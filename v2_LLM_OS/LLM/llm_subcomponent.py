# Imports
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
import requests
import streamlit as st
import pymupdf

load_dotenv()
if not os.environ.get("OPENAI_API_KEY"):
    os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter your OpenAI API Key: ")
model = init_chat_model("o3-mini", model_provider="openai")
embeddings = OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY"), 
                                    model="text-embedding-ada-002")

class LLM:
    def __init__(self, init_prompt):
        self.init_prompt = init_prompt
        self.sensor_name, self.datasheet_chunks = self.__get_datasheet(init_prompt)
        self.vector_db = self.__get_vector_db(self.sensor_name, self.datasheet_chunks)
        self.retriever = self.vector_db.as_retriever()
        self.sensor_parameters = self.__get_sensor_parameters(self.sensor_name, self.retriever)

    def __load_document(self, pdf):
        # Load the PDF document
        loader = PyMuPDFLoader(pdf)
        docs = loader.load()

        chunks = []
        for i, page in enumerate(docs):
            text = page.get_text()
            metadata = {"source": pdf, "page": i + 1}
            chunks.append({"page_content": text, "metadata": metadata})
        return chunks

    def __get_datasheet(self, init_prompt):
        system_prompt = (
            "You are a concise and straightforward Q&A system."
        )
        human_prompt = (
            f"Extract only the I2C sensor name (including brand if breakout board) from this text: {init_prompt}"
        )
        messages = [
            SystemMessage(system_prompt),
            HumanMessage(human_prompt),
        ]
        response = model.invoke(messages)
        sensor_name = response.content
        # sensor_name = "TMP102" #DEBUG PURPOSES
        response = None

        #websearch = mcp9808 datasheet filetype:pdf
        search_query = f"{sensor_name} datasheet filetype:pdf"
        search_results = DDGS().text(search_query)
        if search_results:
            datasheet_url = search_results[0]['href']
            st.write(f"Datasheet URL: {datasheet_url}")
            st.write("Downloading datasheet...")
            response = requests.get(datasheet_url)
            if response.status_code == 200:
                if not os.path.exists(f"/home/steven/FYP/v2_LLM_OS/LLM/Datasheet_DB/{sensor_name}.pdf"):     
                    with open(f"/home/steven/FYP/v2_LLM_OS/LLM/Datasheet_DB/{sensor_name}.pdf", "wb") as file:
                        for chunk in response.iter_content(1024):
                            file.write(chunk)
                    st.write("Datasheet downloaded!")
                else:
                    st.write("Datasheet already exists in the database.")
            st.write("Loading datasheet...")
            chunks = self.__load_document(f"/home/steven/FYP/v2_LLM_OS/LLM/Datasheet_DB/{sensor_name}.pdf")
            st.write("Datasheet loaded!")
        else:
            st.write("No datasheet found for this I2C sensor.")
            return
        
        return sensor_name, chunks

    def __get_vector_db(self, sensor_name, datasheet_chunks):
        if not os.path.exists(f"/home/steven/FYP/v2_LLM_OS/LLM/Datasheet_Vector_DB/{sensor_name}"):
            st.write("Creating Embeddings for Datasheet")

            vector_db = FAISS.from_documents(datasheet_chunks, embeddings)
            vector_db.save_local(f"/home/steven/FYP/v2_LLM_OS/LLM/Datasheet_Vector_DB/{sensor_name}")
            st.write("Embeddings created and saved!")
        else:
            vector_db = FAISS.load_local(f"/home/steven/FYP/v2_LLM_OS/LLM/Datasheet_Vector_DB/{sensor_name}", 
                                        embeddings, allow_dangerous_deserialization=True)
            st.write("Embeddings already exist in the database.")
        
        return vector_db

    def __get_sensor_parameters(self, sensor_name, retriever):
        system_prompt = (
            "You are a concise and straightforward Q&A system. Use the given context to answer the question."
            "{context}"
        )
        prompt = ChatPromptTemplate.from_messages(
            [
                ("system", system_prompt),
                ("human", "{input}"),
            ]
        )
        
        question_answer_chain = create_stuff_documents_chain(model, prompt)
        chain = create_retrieval_chain(retriever, question_answer_chain)

        question = f"Extract only the parameter separated with commas. What parameter does the {sensor_name} measure?"
        response = chain.invoke({"input": question})['answer'].lower()
        response = response.replace(".", "")
        response = response.replace(" ", "")
        parameters = response.split(",")
        return parameters
    
    def __get_oel_init_cmd(self, parameters):
        system_prompt = (
            "You are a concise and straightforward Q&A system. Use the given context to answer the question."
            "{context}"
        )
        prompt = ChatPromptTemplate.from_messages(
            [
                ("system", system_prompt),
                ("human", "{input}"),
            ]
        )
        question_answer_chain = create_stuff_documents_chain(model, prompt)
        chain = create_retrieval_chain(self.retriever, question_answer_chain)

        question = f"Extract only the hex registers needed to initialize {self.sensor_name} sensor? Separate the hex registers with commas. Example: 0x00, 0xA1 or 0x02, 0x23, 0x12."

        if question:
            response = chain.invoke({"input": question})['answer']
            st.write(response)

    def __get_oel_data_len(self, parameters):
        system_prompt = (
            "You are a concise and straightforward Q&A system. Use the given context to answer the question."
            "{context}"
        )
        prompt = ChatPromptTemplate.from_messages(
            [
                ("system", system_prompt),
                ("human", "{input}"),
            ]
        )
        question_answer_chain = create_stuff_documents_chain(model, prompt)
        chain = create_retrieval_chain(self.retriever, question_answer_chain)

        question = f"Extract strictly only the integer of the data length in bytes received from {self.sensor_name} sensor? Example: 2, 6."

        if question:
            response = chain.invoke({"input": question})['answer']
            st.write(response)
        #get the first integer in the response
        return int(response.split()[0])

    def __get_oel_data_format(self, parameters):
        system_prompt = (
            "You are a concise and straightforward Q&A system. Use the given context to answer the question."
            "{context}"
        )
        prompt = ChatPromptTemplate.from_messages(
            [
                ("system", system_prompt),
                ("human", "{input}"),
            ]
        )
        # DATA_KEY_VAL = (0: "HUM", 1: "TEMP");
        # DATA_FORMAT = (0: [12:31], 1: [28:47]);
        # SCALE_FORMAT = (0: "x 100.0 * 1048576.0 / 50.0 - 50.0 +", 1: "x 200.0 * 1048576.0 / 50 -");

        question_answer_chain = create_stuff_documents_chain(model, prompt)
        chain = create_retrieval_chain(self.retriever, question_answer_chain)

        question = f"From the {self.sensor_name} raw data received, what is the order of the sensor parameters? Answer in strings separated by commas. Example: \"temperature\", \"humidity\" or \"temperature\", \"pressure\", \"humidity\"."

        if question:
            response = chain.invoke({"input": question})['answer']
            st.write(response)
        
    def __get_oel_sensor_addr(self):

        # Embed the question
        question_embedding = embeddings.embed("I2C device address")

        # Retrieve relevant document chunks explicitly from FAISS
        retrieved_chunks = self.vector_db.similarity_search_by_vector(question_embedding, k=3)
        
        # Inspect the retrieved chunks (optional, for debugging purposes)
        for idx, chunk in enumerate(retrieved_chunks):
            st.write(f"Retrieved Chunk {idx+1}: {chunk.page_content}")

    
        system_prompt = (
            "You are a helpful assistant. Use the given context to answer the question."
            "{context}"
        )
        prompt = ChatPromptTemplate.from_messages(
            [
                ("system", system_prompt),
                ("human", "{input}"),
            ]
        )

        # Embed the question
        question_embedding = embeddings.embed("I2C device address")

        # Retrieve relevant document chunks explicitly from FAISS
        retrieved_chunks = self.vector_db.similarity_search_by_vector(question_embedding, k=3)
        
        # Inspect the retrieved chunks (optional, for debugging purposes)
        for idx, chunk in enumerate(retrieved_chunks):
            st.write(f"Retrieved Chunk {idx+1}: {chunk.page_content}")



    #public functions
    def get_sensor_parameters(self):
        return self.sensor_parameters
    
    def generate_oel_dict(self, parameters):
        
        oel_code_dict = dict()

        #parts of OEL
        #1. NEW_SENSOR = AHT20
        oel_code_dict["NEW_SENSOR"] = self.sensor_name
        #2. PROTOCOL
        oel_code_dict["PROTOCOL"] = "I2C"
        #3. SENSOR_ADDR
        oel_code_dict["SENSOR_ADDR"] = self.__get_oel_sensor_addr()
        #3. INIT_CMD
        oel_code_dict["INIT_CMD"] = self.__get_oel_init_cmd(parameters)
        #4. DATA_LEN
        oel_code_dict["DATA_LEN"] = self.__get_oel_data_len(parameters)
        #5. DATA_KEY_VAL, DATA_FORMAT, SCALE_FORMAT
        oel_code_dict["DATA_KEY_VAL"], oel_code_dict["DATA_FORMAT"], oel_code_dict["SCALE_FORMAT"] = self.__get_oel_data_format(parameters)
        

        return oel_code_dict