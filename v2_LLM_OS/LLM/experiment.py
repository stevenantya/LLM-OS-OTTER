# Imports
import time
from tracemalloc import start
from typing import final
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain.chains import create_retrieval_chain
from langchain_openai import ChatOpenAI
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from  langchain_community.document_loaders import PyMuPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import getpass
import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, SystemMessage
from duckduckgo_search import DDGS
from openai import responses
import requests
import streamlit as st
import pymupdf
import re
import logging

os.chdir("/home/steven/FYP/v2_LLM_OS/LLM")

log_filename = f"logs/LLM_RAG_{time.strftime('%Y-%m-%d-%H-%M-%S')}.log"
# Set up logging configuration
logger = logging.getLogger()
fhandler = logging.FileHandler(filename=log_filename, mode='a')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fhandler.setFormatter(formatter)
logger.addHandler(fhandler)
logger.setLevel(logging.DEBUG)

load_dotenv()
if not os.environ.get("OPENAI_API_KEY"):
    os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter your OpenAI API Key: ")
model = init_chat_model("o3-mini", model_provider="openai")
logging.debug(f"Loaded model {model}")


def run(sensor_name):
    logging.info(f"Sensor name: {sensor_name}")
    
    start_datasheet_fetch_time = time.time()
    # Find and download sensor datasheet
    search_query = f"{sensor_name} datasheet filetype:pdf"
    search_results = DDGS().text(search_query)
    if search_results:
        datasheet_url = search_results[0]['href']
        logging.debug(f"Datasheet URL: {datasheet_url}")
        logging.debug("Downloading datasheet...")
        if not os.path.exists(f"/home/steven/FYP/v2_LLM_OS/LLM/Datasheet_DB/{sensor_name}.pdf"):
            response = requests.get(datasheet_url)
            if response.status_code == 200:
                with open(f"/home/steven/FYP/v2_LLM_OS/LLM/Datasheet_DB/{sensor_name}.pdf", "wb") as file:
                    for chunk in response.iter_content(1024):
                        file.write(chunk)
                logging.debug("Datasheet downloaded!")
            else: 
                logging.debug("Failed to download datasheet.")
                logging.debug(f"HTTP Status Code: {response.status_code}")
                # terminate the program (should raise exception)
                return
        else:
            logging.debug("Datasheet already exists in the database.")
        logging.debug("Loading datasheet...")
        datasheet_path = f"/home/steven/FYP/v2_LLM_OS/LLM/Datasheet_DB/{sensor_name}.pdf"
        logging.debug("Datasheet loaded!")
    else:
        logging.debug("No datasheet found for this I2C sensor.")
    
    end_datasheet_fetch_time = time.time()
    datasheet_fetch_latency = end_datasheet_fetch_time - start_datasheet_fetch_time
    logging.debug(f"Datasheet fetch latency: {datasheet_fetch_latency} seconds")
    experiment_log.write(f"Datasheet fetch latency: {datasheet_fetch_latency} seconds\n")
        
        
    # Load and partition the datasheet into elements
    # 5 levels of partitioning
    import pymupdf4llm
    import pathlib
    from langchain_text_splitters import RecursiveCharacterTextSplitter, MarkdownTextSplitter
    from langchain_community.document_loaders import UnstructuredMarkdownLoader
    from langchain_core.documents import Document

    start_split_time = time.time()
    
    md_path = f"/home/steven/FYP/v2_LLM_OS/LLM/MD_DB/md_{sensor_name}.md"
    if not os.path.exists(md_path):
        md_text = pymupdf4llm.to_markdown(datasheet_path)
        pathlib.Path(md_path).write_bytes(md_text.encode())
        logging.debug("Datasheet Partition does not exist. Created a new parition")
    else:
        md_text = pathlib.Path(md_path).read_text()
        logging.debug("Datasheet partition exists. Loaded from local file")

    splitter = MarkdownTextSplitter(chunk_size=500, chunk_overlap=100)

    docs = splitter.create_documents([md_text])

    end_split_time = time.time()
    split_latency = end_split_time - start_split_time
    
    logging.debug(len(docs))
    logging.debug(f"Number of chunks: {len(docs)}")
    logging.debug(f"Datasheet partition latency: {split_latency} seconds")
    experiment_log.write(f"Number of chunks: {len(docs)}\n")
    experiment_log.write(f"Datasheet partition latency: {split_latency} seconds\n")


    start_embed_time = time.time()
    
    # Embed the datasheet chunks using FAISS
    #TODO: We might want to use multiple datasheets for the same sensor
    embeddings = OpenAIEmbeddings(
        openai_api_key=os.getenv("OPENAI_API_KEY"), 
        model="text-embedding-ada-002"
    )

    vector_db_path = f"/home/steven/FYP/v2_LLM_OS/LLM/Datasheet_Vector_DB/{sensor_name}"
    if not os.path.exists(vector_db_path):
        vector_db = FAISS.from_documents(docs, embeddings)
        vector_db.save_local(vector_db_path)
        logging.debug("Vector DB not found, created and saved a new Vector DB")
    else:
        vector_db = FAISS.load_local(vector_db_path, embeddings, allow_dangerous_deserialization=True)
        logging.debug("Vector DB found, loaded from local file")
        
    end_embed_time = time.time()
    embed_latency = end_embed_time - start_embed_time
    logging.debug(f"Vector DB embedding latency: {embed_latency} seconds")
    experiment_log.write(f"Vector DB embedding latency: {embed_latency} seconds\n")
        
    
    def retrieve_chunk(query): # Take 10 most similar chunks from the vector DB using cosine simlarity.
        retriever = vector_db.as_retriever(search_type="similarity", search_kwargs={"k": 3})
        retrieved_chunk = retriever.invoke(query)
        return retrieved_chunk
    
    # Iterate through the chunks. Ask the LLM if the chunk is helpful for answering the query. (Chunk validation)
    # How do I ask LLM if the chunk is helpful, if not mark the chunk as not helpful and retrieve the next chunk?
    def validate_chunk(chunks, query):
        # Create a prompt to validate the chunk
        validation_prompt = ChatPromptTemplate.from_template(
            """
            You are an assistant that validates if a provided document chunk is helpful in answering the user's query.

            QUERY:
            {query}

            CHUNK:
            {chunk}

            Is this chunk helpful for answering the query? Respond ONLY with 'Yes' or 'No'.
            """
        )

        validated_chunks = []
        experiment_log.write(f"Retrieved chunk:\n")
        yes_count = 0
        # Inspect the retrieved chunks (optional, for debugging purposes)
        for idx, chunk in enumerate(chunks):
            logging.debug(f"Retrieved Chunk {idx+1}: {chunk.page_content}")
            experiment_log.write(f"     Retrieved Chunk {idx+1}: {chunk.page_content}\n")
            prompt = validation_prompt.format_messages(query=query, chunk=chunk.page_content)
            # logging.debug(prompt)
            validated_response = model.invoke(prompt).content.strip().lower()
            logging.debug(validated_response)
            if 'yes' in validated_response:
                validated_chunks.append(chunk)
                yes_count += 1
                logging.debug("YES. Chunk is helpful, proceeding with the next steps")
            else:
                logging.debug("NO. Chunk not helpful, moving to next chunk")
                continue
        logging.debug(f"Number of helpful chunks: {yes_count}")
        experiment_log.write(f"     Number of helpful chunks: {yes_count}\n")
        return validated_chunks
    
    
    # Consolidate the validated chunks

    def consolidate_chunks(validated_chunks):
        consolidated_chunks = ""
        for idx, chunk in enumerate(validated_chunks):
            consolidated_chunks += f"{idx+1}. {chunk.page_content}\n"
        return consolidated_chunks
    
    def extract_i2c_address(consolidated_chunks, query):
        # Chain of Thought Reasoning LLM to extract the I2C address from the consolidated chunks
        # https://www.datacamp.com/tutorial/chain-of-thought-prompting
        # Create a prompt to extract the I2C address
        extraction_prompt = ChatPromptTemplate.from_template(
            """
            You are a helpful assistant and an expert in I2C Sensors. Assume ideal and default condition.

            Raw context (might be inaccurate):
            {chunk}

            For {sensor_name} sensor, {query} Respond ONLY the hexadecimal value.
            """
        )

        extraction_prompt = extraction_prompt.format_messages(
            chunk=consolidated_chunks,
            sensor_name=sensor_name,
            query=query
        )

        i2c_addr_response = model.invoke(extraction_prompt).content.strip()
        logging.debug(f"Response: {i2c_addr_response}")
        return i2c_addr_response
    
    def extract_i2c_sensor_init_cmd(consolidated_chunks, query):
        #CoT reasoning to extract the I2C address
        prompt_i2c_template = ChatPromptTemplate.from_template(
            """
            You are a helpful assistant and an expert in I2C Sensors. Assume ideal and default condition.

            Raw context (might be inaccurate):
            {chunk}

            From your knowledge of {sensor_name} sensor. {query} Show me the reasoning process step by step and use your memory.
            If neither register addresses nor command codes is needed, please say so. If either one is needed, please say so. If both is needed, please say so.
            """
        )

        prompt_i2c = prompt_i2c_template.format_messages(
            chunk=consolidated_chunks,
            sensor_name=sensor_name,
            query = query
        )

        i2c_CoT_response = model.invoke(prompt_i2c).content.strip()
        logging.debug(f"Response: {i2c_CoT_response}")

        # Feedback to get hexadecimal values
        prompt_i2c_feedback_template = ChatPromptTemplate.from_template(
            """
            You are a helpful assistant and an expert in I2C Sensors. Assume ideal and default condition.

            My expert told me:
            {i2c_CoT_response}

            {query} Sequentially, What read command or register hexadecimal value does that? Which register address should be pointed to to do that?
            If both is not needed, output "INOP", or else
            Finish the sentence, the hexadecimal values are:
            """
        )

        prompt_i2c_feedback = prompt_i2c_feedback_template.format_messages(
            i2c_CoT_response=i2c_CoT_response,
            sensor_name=sensor_name,
            query = query
        )
        i2c_feedback_response = model.invoke(prompt_i2c_feedback).content.strip()
        logging.debug(f"Response: {i2c_feedback_response}")

        if "INOP" in i2c_feedback_response:
            logging.debug("No initialization needed")
            return "INOP"

        else:
            # Cleanup the response to get only the hexadecimal values
            prompt_i2c_cleanup_template = ChatPromptTemplate.from_template(
                """
                You are a helpful assistant and hexadecimal values extractor.

                My expert told me:
                {i2c_feedback_response}

                Extract only the hexadecimal values. Output it in sequence of 1 bytes. You may convert larger bytes into multiple 1 bytes if needed. Separate the values by commas.
                0x...
                """
            )
            prompt_i2c_cleanup = prompt_i2c_cleanup_template.format_messages(
                i2c_feedback_response=i2c_feedback_response
            )
            i2c_cleanup_response = model.invoke(prompt_i2c_cleanup).content.strip()
            logging.debug(f"Response: {i2c_cleanup_response}")

            return i2c_cleanup_response
    
    
    def get_trigger_command(model, chunk, sensor_name):
        query_trigger = "Does the sensor require a command or register value to trigger measurement?"
        trigger_prompt = ChatPromptTemplate.from_template(
            """
            You are a helpful assistant and an expert in I2C Sensors. Assume ideal and default condition.

            Raw context (might be inaccurate):
            {chunk}

            From your knowledge. For {sensor_name} sensor: {query}
            Explain step-by-step reasoning. If no trigger is needed, say "INOP".
            """
        )

        formatted_trigger = trigger_prompt.format_messages(
            chunk=chunk, sensor_name=sensor_name, query=query_trigger
        )
        CoT_trigger_response = model.invoke(formatted_trigger).content.strip()

        feedback_prompt = ChatPromptTemplate.from_template(
            """
            You are a helpful assistant and expert in I2C Sensors.

            My expert said:
            {CoT_response}

            Does a trigger command exist? If not, say "INOP". 
            Otherwise, finish the sentence: The hexadecimal values are:
            """
        )

        trigger_feedback = feedback_prompt.format_messages(CoT_response=CoT_trigger_response)
        trigger_final = model.invoke(trigger_feedback).content.strip()
        return trigger_final


    def get_read_registers(model, chunk, sensor_name):
        query_register = "Which register(s) should be read to get measurement data?"
        register_prompt = ChatPromptTemplate.from_template(
            """
            You are a helpful assistant and an expert in I2C Sensors. Assume ideal and default condition.

            Raw context (might be inaccurate):
            {chunk}

            For {sensor_name} sensor: {query}
            Explain reasoning. If no register read is needed, say "INOP".
            """
        )

        formatted_register = register_prompt.format_messages(
            chunk=chunk, sensor_name=sensor_name, query=query_register
        )
        CoT_register_response = model.invoke(formatted_register).content.strip()

        feedback_prompt = ChatPromptTemplate.from_template(
            """
            You are a helpful assistant and expert in I2C Sensors.

            My expert said:
            {CoT_response}

            Do I need to read specific registers? If not, say "INOP". 
            Otherwise, finish the sentence: The hexadecimal values are:
            """
        )

        register_feedback = feedback_prompt.format_messages(CoT_response=CoT_register_response)
        register_final = model.invoke(register_feedback).content.strip()
        return register_final


    def extract_hex_values(model, response_text):
        cleanup_prompt = ChatPromptTemplate.from_template(
            """
            You are a helpful assistant and hexadecimal values extractor.

            My expert told me:
            {response_text}

            Extract only the hexadecimal values as individual 1-byte entries, separated by commas.
            Start with 0x...
            """
        )

        cleanup_msg = cleanup_prompt.format_messages(response_text=response_text)
        hex_output = model.invoke(cleanup_msg).content.strip()
        return hex_output


    def extract_i2c_sensor_read_cmd(consolidated_chunks, query):
        trigger_response = get_trigger_command(model, consolidated_chunks, sensor_name)
        register_response = get_read_registers(model, consolidated_chunks, sensor_name)

        if "INOP" in trigger_response and "INOP" in register_response:
            logging.debug("No trigger or read register needed.")
            return "INOP"

        result = []
        if "INOP" not in trigger_response:
            hex_trigger = extract_hex_values(model, trigger_response)
            result.append(hex_trigger)
        else:
            hex_trigger = None

        if "INOP" not in register_response:
            hex_register = extract_hex_values(model, register_response)
            result.append(hex_register)
        else:
            hex_register = None
        
        combined_hex = ", ".join(result)
        logging.debug(f"Combined I2C Read Command: {combined_hex}")
        
        # 🔍 FINAL VALIDATION PROMPT
        final_check_prompt = ChatPromptTemplate.from_template(
            """
            You are a helpful assistant and I2C sensor expert.

            Sensor: {sensor_name}

            Based on the following parsed results:
            - Trigger command bytes (if any): {hex_trigger}
            - Register read bytes (if any): {hex_register}

            Combined into this final I2C sequence:
            {combined_hex}

            Is this the correct sequence of hexadecimal values to initiate and read measurement from the sensor under default/ideal conditions?
            - If yes, ONLY say: "yes"
            - If no, ONLY say THE CORRECT sequence of hexadecimal values. DO NOT give explanation. 
            0x...
            """
        )

        final_check = final_check_prompt.format_messages(
            sensor_name=sensor_name,
            hex_trigger=hex_trigger if hex_trigger else "INOP",
            hex_register=hex_register if hex_register else "INOP",
            combined_hex=combined_hex
        )

        final_hex_response = model.invoke(final_check).content.strip()
        logging.debug(f"Final Hex Check Response: {final_hex_response}")

        if 'yes' in final_hex_response.lower():
            return combined_hex
        else:
            return final_hex_response
        

# The old extract_i2c_sensor_read_cmd function is commented out below    
    '''
    def extract_i2c_sensor_read_cmd(consolidated_chunks, query):
        query = "What read command or register hexadecimal value triggers a sensor measurement? Which register address should be pointed to or read from to acquire data?"
        #CoT reasoning to extract the I2C address
        prompt_i2c_template = ChatPromptTemplate.from_template(
            """
            You are a helpful assistant and an expert in I2C Sensors. Assume ideal and default condition.

            Raw context (might be inaccurate):
            {chunk}

            From your knowledge. For {sensor_name} sensor. {query} Show me the reasoning process step by step and use your memory.
            If neither pointing to register addresses, reading from register addresses, nor sending trigger command codes is needed, please say so. If either one is needed, please say so. If more than one or all is needed, please say so.
            """
        )

        prompt_i2c = prompt_i2c_template.format_messages(
            chunk=consolidated_chunks,
            sensor_name=sensor_name,
            query = query
        )

        CoT_response = model.invoke(prompt_i2c).content.strip()
        logging.debug(f"Response: {CoT_response}")

        # Feedback to get hexadecimal values
        prompt_i2c_feedback_template = ChatPromptTemplate.from_template(
            """
            You are a helpful assistant and an expert in I2C Sensors. Assume ideal and default condition.

            My expert told me:
            {i2c_CoT_response}

            {query}
            If nothing is needed, output "INOP", or else
            Finish the sentence, the hexadecimal values are: 
            """
        )

        prompt_i2c_feedback = prompt_i2c_feedback_template.format_messages(
            i2c_CoT_response=CoT_response,
            sensor_name=sensor_name,
            query = query
        )
        i2c_feedback_response = model.invoke(prompt_i2c_feedback).content.strip()
        logging.debug(f"Response: {i2c_feedback_response}")


        if "INOP" in i2c_feedback_response:
            
            prompt_i2c_catch_error_template = ChatPromptTemplate.from_template(
                """
                You are a helpful assistant and an expert in I2C Sensors. Assume ideal and default condition.

                My expert told me:
                {i2c_feedback_response}

                I understand that we do not need trigger command. My question now is, do I need to point to or read from specific register addresses?
                If so please tell me the hexadecimal values of the registers to read from! If not, please say INOP!
                """
            )

            prompt_i2c_catch_error = prompt_i2c_catch_error_template.format_messages(
                i2c_feedback_response=i2c_feedback_response
            )
            
            i2c_feedback_response = model.invoke(prompt_i2c_catch_error).content.strip()
            logging.debug(f"Response: {i2c_feedback_response}")
            
            if "INOP" in i2c_feedback_response:
                logging.debug("No read command needed")
                return "INOP"
        
        # Cleanup the response to get only the hexadecimal values
        prompt_i2c_cleanup_template = ChatPromptTemplate.from_template(
            """
            You are a helpful assistant and hexadecimal values extractor.

            My expert told me:
            {i2c_feedback_response}

            Extract only the hexadecimal values. Output it in sequence of 1 bytes. You may convert larger bytes into multiple 1 bytes if needed. Separate the values by commas.
            0x...
            """
        )
        prompt_i2c_cleanup = prompt_i2c_cleanup_template.format_messages(
            i2c_feedback_response=i2c_feedback_response
        )
        i2c_cleanup_response = model.invoke(prompt_i2c_cleanup).content.strip()
        logging.debug(f"Response: {i2c_cleanup_response}")

        return i2c_cleanup_response
    '''
    
    
    def extract_i2c_sensor_data_len(consolidated_chunks, query):
        # CoT reasoning to extract the data length
        prompt_i2c_template = ChatPromptTemplate.from_template(
            """
            You are a helpful assistant and an expert in I2C Sensors. Assume ideal and default condition.

            Raw context (might be inaccurate):
            {chunk}

            From your knowledge, {sensor_name} sensor data output length in bytes? Show me the reasoning process step by step and use your memory.
            """
        )

        prompt_i2c = prompt_i2c_template.format_messages(
            chunk=consolidated_chunks,
            sensor_name=sensor_name
        )

        CoT_response = model.invoke(prompt_i2c).content.strip()
        logging.debug(f"Response: {CoT_response}")

        # Feedback to get length in bytes
        prompt_i2c_feedback_template = ChatPromptTemplate.from_template(
            """
            You are a helpful assistant and an expert in I2C Sensors. Assume ideal and default condition.

            My expert told me:
            {i2c_CoT_response}

            What are the {sensor_name} sensor data output length in bytes?
            ONLY fill in this sentence, the sensor data output length is X bytes
            """
        )

        prompt_i2c_feedback = prompt_i2c_feedback_template.format_messages(
            i2c_CoT_response=CoT_response,
            sensor_name=sensor_name
        )
        i2c_feedback_response = model.invoke(prompt_i2c_feedback).content.strip()
        logging.debug(f"Response: {i2c_feedback_response}")

        # Cleanup the response to get only the numerical values
        prompt_i2c_cleanup_template = ChatPromptTemplate.from_template(
            """
            You are a helpful assistant and values extractor.

            My expert told me:
            {i2c_feedback_response}

            Extract only the numerical byte value.
            """
        )
        prompt_i2c_cleanup = prompt_i2c_cleanup_template.format_messages(
            i2c_feedback_response=i2c_feedback_response
        )
        i2c_cleanup_response = model.invoke(prompt_i2c_cleanup).content.strip()
        logging.debug(f"Response: {i2c_cleanup_response}")

        # Extract the first integer using regex
        match = re.search(r"\b\d+\b", i2c_cleanup_response)
        first_integer = match.group() if match else None

        logging.debug(f"First Integer Extracted: {first_integer}")
        return first_integer

    
    def extract_i2c_data_key_val(consolidated_chunks, size, query):
        prompt_i2c_template = ChatPromptTemplate.from_template(
            """
            You are a helpful assistant and an expert in I2C Sensors. Assume ideal and default condition.

            Raw context (might be inaccurate):
            {chunk}

            1. What physical quantities or parameters does the {sensor_name} measure? {query}
            2. Assuming `raw_bytes` is a `{size}`-byte array read from the sensor register, specify the **bit position range** for each physical parameter using the format: `ParameterName[high_bit:low_bit]`.  
            For example: `Temperature[11:0]` indicates the parameter spans bits 11 down to 0 (with 11 being the most significant bit).
            3. The `raw_bytes` array is encoded in **big-endian** format — the most significant byte appears first.
            4. Omit anything unrelated to raw data output, such as alert pins, config registers, or CRC.
            5. Do **not** describe MSB/LSB or byte-level layout — focus on the full bit range for each parameter, as if all bytes have already been concatenated into a single binary stream.
            6. Please explain your reasoning step by step, using both the provided context and your internal knowledge.
            """
        )

        prompt_i2c = prompt_i2c_template.format_messages(
            chunk=consolidated_chunks,
            sensor_name=sensor_name,
            size=size,
            query=query
        )

        CoT_response = model.invoke(prompt_i2c).content.strip()
        logging.debug(f"Response: {CoT_response}")

        prompt_i2c_feedback_template = ChatPromptTemplate.from_template(
            """
            You are a helpful assistant and an expert in I2C sensors. Assume ideal and default condition.

            My expert told me:
            {i2c_CoT_response}

            From the above explanation, extract only the **measurement parameters** and their corresponding bit ranges.

            ONLY FILL IN the sentence:
            The measurement values are arranged as: (ParameterName_1: [high_bit_1:low_bit_1], ParameterName_2: [high_bit_2:low_bit_2], ...)

            Notes:
            - Only include parameters that represent physical quantities (e.g., Temperature, Humidity, Pressure).
            - Format each parameter in the exact syntax: `ParameterName: [high_bit:low_bit]`.
            - Ensure bit indices are integers and in decreasing order (high_bit > low_bit).
            - If there is any ambiguity, infer based on standard sensor conventions or leave out that parameter.
            
            """
        )

        prompt_i2c_feedback = prompt_i2c_feedback_template.format_messages(
            i2c_CoT_response=CoT_response,
            sensor_name=sensor_name
        )
        i2c_feedback_response = model.invoke(prompt_i2c_feedback).content.strip()
        logging.debug(f"Response: {i2c_feedback_response}")


        prompt_i2c_cleanup_template = ChatPromptTemplate.from_template(
            """
            You are a helpful assistant and an expert in I2C sensors. Assume ideal and default condition.

            My expert told me:
            {i2c_feedback_response}

            Normalize the measurement bit arrangements to the final standard format.

            ONLY FILL IN the sentence:
            The raw measurement values are arranged as: (ParameterName_1: [high_bit_1:low_bit_1], ParameterName_2: [high_bit_2:low_bit_2], ...)

            Rules:
            - Only include physical measurement parameters (ignore config, alert, CRC, etc.).
            - If a parameter spans multiple bytes, **collapse the range** to just the highest and lowest bit (e.g., from 15 down to 0 → `[15:0]`).
            - Format each entry precisely as: `ParameterName: [high_bit:low_bit]` with no extra description.
            - Output as a single, comma-separated tuple enclosed in parentheses.

            """
        )
        prompt_i2c_cleanup = prompt_i2c_cleanup_template.format_messages(
            i2c_feedback_response=i2c_feedback_response
        )
        i2c_cleanup_response = model.invoke(prompt_i2c_cleanup).content.strip()
        logging.debug(f"Response: {i2c_cleanup_response}")

        # Extract only content within parentheses
        matches = re.findall(r'\((.*?)\)', i2c_cleanup_response)

        extracted_content = matches[0] if matches else ""
        extracted_content = "(" + extracted_content + ")"
        logging.debug(f"Response: {extracted_content}")

        return extracted_content


    def extract_i2c_sensor_data_scale_format(consolidated_chunks, sensor_data_key_val, query):
        query = "What is the formula or process for converting raw sensor output values to physical units like temperature, humidity, pressure, or altitude?"
        logging.debug(f"Sensor data key value: {sensor_data_key_val}")
        
        prompt_i2c_template = ChatPromptTemplate.from_template(
            """
            You are a helpful assistant and an expert in I2C sensors. Assume the sensor is operating under normal room conditions.

            Raw context (might be inaccurate — please verify carefully):
            {chunk}

            {query}
            Create a MATH formula to convert the raw `{sensor_name}` sensor output into physical units.

            Bit Mapping:
            Each parameter has been extracted from the raw sensor data based on the following bit ranges:  
            {sensor_data_key_val}  
            For example: `Temperature: [11:0]` means bits 11 down to 0 were extracted.

            Rules:
            1. The extracted bits for each parameter are stored as a `uint32_t` variable named `x`.
            2. Use only arithmetic, bitwise, and modulo operators. DO NOT use any IF statements or control flow. DO NOT use XOR.
            3. DO NOT use hexadecimal or binary literals. Use **decimal or float numbers only**
            4. ONLY use `x` as the variable in your formula.
            5. For each parameter, provide a mathematical formula to convert `x` into physical units.
            6. Explain your reasoning step by step, using both the provided context and your internal knowledge of the sensor behavior and datasheet conventions.

            """
        )

        prompt_i2c = prompt_i2c_template.format_messages(
            chunk=consolidated_chunks,
            sensor_name=sensor_name,
            sensor_data_key_val = sensor_data_key_val,
            query = query
        )

        CoT_response = model.invoke(prompt_i2c).content.strip()
        logging.debug(f"Response: {CoT_response}")

        
        result = re.sub(r':\s*\[[^\]]*\]', '', sensor_data_key_val)
        stripped_sensor_data_key_val = result
        
        prompt_i2c_feedback_template = ChatPromptTemplate.from_template(
            """
            You are a helpful assistant and an expert in I2C sensors. Assume the sensor is operating under normal room conditions.

            My expert told me:
            {i2c_CoT_response}

            Now convert the explanation above into **reverse polish notation (RPN)** formulas for each parameter defined in:
            {sensor_data_key_val}  

            Instructions:
            - Use `X` as the variable representing the extracted raw bits.
            - Convert any hexadecimal values to decimal.
            - Use standard programming bitwise operators: `>>`, `<<`, `&`, `|`.
            - Use RPN format: each token (number, variable, operator) is space-separated and postfix (e.g., `X 2 >> 0.0625 *`).
            - Provide **one RPN formula per parameter** listed in `{sensor_data_key_val}`.
            - If a parameter is missing or unclear, leave it out.

            ONLY output the reverse polish notations for each parameter.
            """
        )

        prompt_i2c_feedback = prompt_i2c_feedback_template.format_messages(
            i2c_CoT_response=CoT_response,
            sensor_name=sensor_name,
            sensor_data_key_val = stripped_sensor_data_key_val
        )
        i2c_feedback_response = model.invoke(prompt_i2c_feedback).content.strip()
        logging.debug(f"Response: {i2c_feedback_response}")
        
        

        prompt_i2c_cleanup_template = ChatPromptTemplate.from_template(
            """
            You are a helpful assistant and an expert in I2C sensors. Assume the sensor is operating under normal room conditions.

            My expert told me:
            {i2c_feedback_response}

            Now represent each parameter from the following mapping:  
            {sensor_data_key_val}  
            as a key-value pair with its reverse polish notation (RPN) conversion formula.

            Rules:
            - X is the variable representing the raw extracted value.
            - Use RPN syntax: tokens are space-separated and postfix (e.g., `X 2 >> 0.01 * 50 +`).
            - Use standard bitwise operators (`>>`, `<<`, `&`, `|`) as needed.
            - ONLY FILL IN the sentence below:

            The measurement values are arranged as: (parameter1: "reverse_polish_notation1", parameter2: "reverse_polish_notation2", ...)
            """
        )
        prompt_i2c_cleanup = prompt_i2c_cleanup_template.format_messages(
            i2c_feedback_response=i2c_feedback_response,
            sensor_data_key_val = stripped_sensor_data_key_val
        )
        i2c_cleanup_response = model.invoke(prompt_i2c_cleanup).content.strip()
        logging.debug(i2c_cleanup_response)

        # Extract only content within parentheses
        matches = re.findall(r'\((.*?)\)', i2c_cleanup_response)
        matches = [re.sub(r'[–—]', '-', match) for match in matches]
        
        extracted_content = matches[0] if matches else i2c_cleanup_response
        extracted_content = "(" + extracted_content + ")"
        logging.debug(f"Response: {extracted_content}")

        return extracted_content


    def convert_to_array_indexing(s, size):
        # Convert the string to array indexing format
        # From (ParameterName_1: [high_bit_1:low_bit_1], ParameterName_2: [high_bit_2:low_bit_2], ...)
        # To (ParameterName_1: [array_start_index_1:array_end_index_1], ParameterName_2: [array_start_index_2:array_end_index_2], ...)
        # Example: "(Temperature: [15:4], ...)" to "(Temperature[0:11], ...)"
        size = int(size)  # Ensure size is treated as an integer
        total_bits = size * 8
        result = []

        # Extract all (Parameter: [high:low]) pairs
        pattern = r'(\w+):\s*\[(\d+):(\d+)\]'
        matches = re.findall(pattern, s)

        for param, high, low in matches:
            high = int(high)
            low = int(low)

            # Convert to array indexing (from left to right in big-endian)
            array_start = total_bits - 1 - high
            array_end = total_bits - 1 - low

            result.append(f"{param}: [{array_start}:{array_end}]")

        return f"({', '.join(result)})"
        return result

    functions = [
        extract_i2c_address,
        extract_i2c_sensor_init_cmd,
        extract_i2c_sensor_read_cmd,
        extract_i2c_sensor_data_len,
        extract_i2c_data_key_val,
        extract_i2c_sensor_data_scale_format
    ]

    def main():
        responses = []
        latency = dict()
        with open(f"logs/OUT_LLM_RAG_{time.strftime('%Y-%m-%d-%H-%M-%S')}.txt", "w") as f:
            f.write(f"Sensor name: {sensor_name}\n")
            for query, function in zip(queries, functions):
                latency[query] = dict()
                experiment_log.write(f"Query: {query}\n")
                logging.info(f"Query: {query}")
                print(f"Query: {query}")
                f.write(f"Query: {query}\n")
                
                start_retrieve_time = time.time()
                retrieved_chunk = retrieve_chunk(query)
                end_retrieve_time = time.time()
                retrieve_latency = end_retrieve_time - start_retrieve_time
                latency[query]["retrieve_chunk"] = retrieve_latency
                
                
                start_validate_time = time.time()
                validated_chunks = validate_chunk(retrieved_chunk, query)
                end_validate_time = time.time()
                validate_latency = end_validate_time - start_validate_time
                latency[query]["validate_chunk"] = validate_latency
                
                
                consolidated_chunks = consolidate_chunks(validated_chunks)
                experiment_log.write(f"Consolidated Final chunk: {consolidated_chunks}\n")
                
                start_function_time = time.time()
                if function == extract_i2c_sensor_data_len:
                    response = function(consolidated_chunks, query)
                    sensor_data_len = response
                elif function == extract_i2c_data_key_val:
                    response = function(consolidated_chunks, sensor_data_len, query)
                    sensor_data_key_val = response
                    response = convert_to_array_indexing(response, sensor_data_len)
                elif function == extract_i2c_sensor_data_scale_format:
                    response = function(consolidated_chunks, sensor_data_key_val, query)
                else:
                    response = function(consolidated_chunks, query)
                end_function_time = time.time()
                function_latency = end_function_time - start_function_time
                latency[query]["function"] = function_latency
                
                responses.append(response)
                logging.info(f"Response: {response}")
                print(f"Response: {response}")
                f.write(f"Response: {response}\n")
                logging.info("\n")
                print("\n")

                retrieved_chunk = None
                validated_chunks = None
                consolidated_chunks = None
                response = None
        return responses, latency
    responses_out, latency_out = main()
    return responses_out, latency_out
    
queries = [
    "What is the I2C address hexadecimal value?",
    "How do you initialize or reset the sensor? Include register addresses or command codes for initialization or soft reset or power-up.",
    "What read command or register hexadecimal value triggers a sensor measurement? Which register address should be pointed to or read from to acquire data?",
    "What is the sensor data output length in bytes?",
    "Where are the sensor measurement values stored in registers or memory? Include register addresses, byte ranges, or bit positions.",
    "What is the formula or process for converting raw sensor output values to physical units like temperature, humidity, pressure, or altitude?",
]

if __name__ == "__main__":
    # Example usage
    # Start time
    
    for i in range(9):
        print(f"Running experiment {i}...")
            
        # sensor_names = ["SHT31"]
        sensor_names = ["AHT20", "MCP9808", "SHT31", "TMP102"]
        beg_for_time = time.time()
        for sensor_name in sensor_names:
            with open(f"experiment_logs/{sensor_name}_{time.strftime('%Y-%m-%d-%H-%M-%S')}.txt", "w") as experiment_log:
                start_time = time.time()
                print(f"Running experiment for sensor: {sensor_name}, start time: {start_time}")
                responses, latency = run(sensor_name)
                for query, response in zip(queries, responses):
                    experiment_log.write(f"Query: {query}\n")
                    experiment_log.write(f"Response: {response}\n")
                for key in latency:
                    experiment_log.write(f"Latency for {key}:\n")
                    for sub_key in latency[key]:
                        experiment_log.write(f"     {sub_key}: {latency[key][sub_key]} seconds\n")
                end_time = time.time()
                latency = end_time - start_time
                print(f"Ended experiment for sensor: {sensor_name}, ran for: {latency}. end time: {end_time}")
                logging.info(f"Latency: {latency} seconds")
                experiment_log.write(f"Latency: {latency} seconds\nEnd time: {end_time}\n")
                
        end_for_time = time.time()
        total_latency = end_for_time - beg_for_time
        logging.info(f"Total Latency: {total_latency} seconds\nEnd time: {end_for_time}")
        print(f"Total Latency: {total_latency} seconds\nEnd time: {end_for_time}")
        
        time.sleep(5)