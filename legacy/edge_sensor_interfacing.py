# edge_sensor_interfacing.py
# Functions as the 
# 1. CLI for the user to input commands.
# 2. Relaying to Large Language Model the input command
# 3. Receives the output command from LLM (Encoded in a language that the microcontroller understands)
# 4. Sends the command to Microcontroller via Serial. (Essentially an encoded command)
# 5. Reads the sensor output


import serial
import time
import datetime
import os
from typing import List, Optional
import json

from pydantic import BaseModel
from groq import Groq
from openai import OpenAI

groq_client = Groq(
    api_key = os.environ.get("GROQ_API_KEY"),
)
openai_client = OpenAI(
    api_key = os.environ.get("OPENAI_API_KEY"),
)
timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H:%M:%S')
timestamp = timestamp.replace(':', '_')
# Function 1. CLI for the user to input commands.
def user_cli():
    print("Edge Sensor Interfacing")
    global sensor_name
    global port_number
    sensor_name = input("Enter the name of the sensor you want to interface with: ")
    port_number = input("Enter the port number of the sensor: ")
    return

def groq_post():
    chat_completion = groq_client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are an embedded system expert. I will give you a sensor model. Output exactly in\
                            this manner. Sensor name, Sensor address, Sensor register address,\
                            post processing(in Math format). rawData is 16 bit value of the MSB\
                            and LSB. rawData = Wire.read() « 8 — Wire.read()",
            },
            {
                "role": "user",
                "content": "ADT7410",
            },
            {
                "role": "system",
                "content": "ADT7410, 0x48, 0x00, rawData/128",
            },
            {
                "role": "user",
                "content": "MCP9808,",
            },
            {
                "role": "system",
                "content": "MCP9808, 0x18, 0x05, ((rawData & 4095) - (rawData & 4096)) /16",
            },
            {
                "role": "user",
                "content": f"${sensor_name}",
            }
        ],
        model = "llama-3.3-70b-versatile",
        temperature=0,
        max_completion_tokens=1024,
        top_p = 0.5,
        stop=". ",
        stream=False,
    )
    print(chat_completion.choices[0].message.content)

def groq_post_json():
    class Sensor(BaseModel):
        sensor_name: str
        sensor_address: str
        sensor_register_address: str
        post_processing: str
    
    def groq_post_json_res() -> Sensor:
        chat_completion = groq_client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "You are an embedded system expert. I will give you a sensor model. Output exactly in\
                                this manner. Sensor name, Sensor address, Sensor register address,\
                                post processing(in Math format). rawData is 16 bit value of the MSB\
                                and LSB. rawData = Wire.read() « 8 — Wire.read(). Your output is in JSON\n"
                                f" The JSON object must use the schema: {json.dumps(Sensor.model_json_schema(), indent=2)}",
                },
                {
                    "role": "user",
                    "content": f"${sensor_name}",
                },
            ],
            model="llama-3.3-70b-versatile",
            temperature=0,
            # Streaming is not supported in JSON mode
            stream=False,
            # Enable JSON mode by setting the response format
            response_format={"type": "json_object"},
        )
        return Sensor.model_validate_json(chat_completion.choices[0].message.content)

def gpt_post():
    chat_completion = openai_client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "developer",
                "content": "You are an embedded system expert. I will give you a sensor model. Output exactly in\
                            this manner. Sensor name, Sensor address, Sensor register address,\
                            post processing(in Math format). rawData is 16 bit value of the MSB\
                            and LSB. rawData = Wire.read() « 8 — Wire.read()",
            },
            {
                "role": "user",
                "content": "ADT7410",
            },
            {
                "role": "assistant",
                "content": "ADT7410, 0x48, 0x00, rawData/128",
            },
            {
                "role": "user",
                "content": "MCP9808,",
            },
            {
                "role": "assistant",
                "content": "MCP9808, 0x18, 0x05, ((rawData & 4095) - (rawData & 4096)) /16",
            },
            {
                "role": "user",
                "content": f"${sensor_name}",
            }
        ],
    )
    print(chat_completion.choices[0].message.content)

def gpt_post_json():
    class Sensor(BaseModel):
        sensor_name: str
        sensor_address: str
        sensor_register_address: str
        post_processing: str
    
    def gpt_post_json_res() -> Sensor:
        chat_completion = openai_client.beta.chat.completions.parse(
            model="o1-2024-12-17",
            messages=[
                {
                    "role": "system",
                    "content": "You are an embedded system expert. I will give you a sensor model. Output exactly in\
                                this manner. Sensor name, Sensor address, Sensor register address,\
                                post processing(in Math format). rawData is 16 bit value of the MSB\
                                and LSB. rawData = Wire.read() « 8 — Wire.read(). Your output is in JSON\n",
                },
                {
                    "role": "user",
                    "content": f"${sensor_name}",
                },
                response_format=Sensor,
            ],
           
        )
        event = chat_completion.choices[0].message.parsed
        return event


# Function 2. Relaying to Large Language Model the input command
def llm_post():
    print("Please choose your preferred large language model\n\
          1. Llama 3.3 70b\n\
          2. GPT o1\n")
    isValidChoice = False
    llm_choice = ''
    while isValidChoice == False:
        llm_choice = input("Enter your choice: ")
        if llm_choice == '1':
            print("You have chosen Llama 3.3 70b")
            isValidChoice = True
        elif llm_choice == '2':
            print("You have chosen GPT o1")
            isValidChoice = True
        else:
            print("Invalid choice. Please enter a valid choice")
    
    if llm_choice == '1':
        groq_mode = input("Please enter 1. Normal Mode or 2. JSON Mode: ")
        if groq_mode == '1':
            output = groq_post()
        elif groq_mode == '2':
            json_output = groq_post_json()
        else:
            print("Invalid choice. Please enter a valid choice")
    elif llm_choice == '2':
        gpt_mode = input("Please enter 1. Normal Mode or 2. JSON Mode: ")
        if gpt_mode == '1':
            output = gpt_post()
        elif gpt_mode == '2':
            json_output = gpt_post_json()
        else:
            print("Invalid choice. Please enter a valid choice")

    if groq_mode == '1' or gpt_mode == '1':
        return (output, 1)
    else:
        return (json_output, 2)

# Function 4. Sends the command to Microcontroller via Serial. (Essentially an encoded command)
PORT = 'COM3'
BAUDRATE = 9600
TIMEOUT = 1
FILENAME = f"edge_sensor_data_{timestamp}.txt"

def process_json(json_data):
    str = "" + json_data.sensor_name + "," + json_data.sensor_address + "," + json_data.sensor_register_address + "," + json_data.post_processing
    return str

def mcu_write(llm_output):
    if llm_output[1] == 1:
        data = llm_output[0]
    elif llm_output[1] == 2:
        data = process_json(llm_output[0])

    ser = serial.Serial(PORT, BAUDRATE, timeout=TIMEOUT)
    ser.write(data)
    ser.close()

# Function 5. Reads the sensor output
def mcu_read():
    ser = serial.Serial(PORT, BAUDRATE, timeout=TIMEOUT)
    if ser.in_waiting > 0:
        response = ser.readline().decode('utf-8').strip()
        print(response)
        return response
    return None

with open(FILENAME, 'wt') as f:
    f.write('\n')

def main():
    user_cli()
    llm_output = llm_post()
    mcu_write(llm_output)

if __name__ == '__main__':
    main()