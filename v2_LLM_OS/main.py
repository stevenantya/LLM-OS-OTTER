from LLM import llm_subcomponent
import streamlit as st
from rapidfuzz import process

global llm_obj 

def i2c_query():
    sensor_prompt = st.text_input("What i2c sensor you want to interface with?")
    if sensor_prompt:
        return sensor_prompt

def parameter_query(llm_obj):
    parameters = llm_obj.get_sensor_parameters()
    st.write("Supported parameters:", parameters)
    parameter_prompt = st.text_input("What parameter do you want to measure?")
    return parameter_prompt

def process_parameter(llm_obj, parameter_prompt):
    parameters = llm_obj.get_sensor_parameters()
    words = parameter_prompt.lower().split()
    # Match words against parameters with a similarity threshold
    matched_params = set()
    for word in words:
        best_match = process.extractOne(word, parameters, score_cutoff=70)
        if best_match:
            matched_params.add(best_match[0])

    unsupported_params = [word for word in words if word not in matched_params]

    if matched_params:
        print("Supported parameters:", list(matched_params))
    if unsupported_params:
        print("Warning: Some parameters are not supported:", unsupported_params)

if __name__ == "__main__":
    st.title("OTTER LLM OS Front-End")
    sensor_prompt = st.text_input("What i2c sensor (include breakout board brand) you want to interface with?")
    if sensor_prompt:
        #initialize the llm object 
        #members: sensor_name, datasheet_chunks, vector_db, retriever, sensor_parameters
        llm_obj = llm_subcomponent.LLM(sensor_prompt)

        #answer when asked about the sensor parameters
        parameter_prompt = parameter_query(llm_obj)

        #sensor parameters: temperature, humidity, pressure, etc.
        parameters = process_parameter(llm_obj, parameter_prompt)

        oel = llm_obj.generate_oel_dict(parameters)
