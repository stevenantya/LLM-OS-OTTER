import os
import re
import csv
import glob
from pathlib import Path
folder_path = "/home/steven/FYP/v2_LLM_OS/LLM/experiment_logs"


# Folder with .txt files
folder = Path(folder_path)

# List of target queries (exact matches)
target_queries = [
    "Query: What is the I2C address hexadecimal value?",
    "Query: How do you initialize or reset the sensor? Include register addresses or command codes for initialization or soft reset or power-up.",
    "Query: What read command or register hexadecimal value triggers a sensor measurement? Which register address should be pointed to or read from to acquire data?",
    "Query: What is the sensor data output length in bytes?",
    "Query: Where are the sensor measurement values stored in registers or memory? Include register addresses, byte ranges, or bit positions.",
    "Query: What is the formula or process for converting raw sensor output values to physical units like temperature, humidity, pressure, or altitude?"
]

# For storing results
all_results = {}

# Loop through each file
for txt_file in folder.glob("*.txt"):
    with open(txt_file, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f.readlines()]

    result = {}
    for i, line in enumerate(lines):
        if line in target_queries and i + 1 < len(lines):
            response_line = lines[i + 1]
            if response_line.startswith("Response:"):
                result[line] = response_line[len("Response:"):].strip()
    
    all_results[txt_file.name] = result

# Store output rows for CSV
csv_rows = []

# Loop through all results again to regenerate final OEL codes
for file, qa_pairs in all_results.items():
    base_name = Path(file).stem
    sensor_name = base_name.split("_")[0]
    OEL_OUT = [None] * 7

    for question, answer in qa_pairs.items():
        match question:
            case "Query: What is the I2C address hexadecimal value?":
                hex_match = re.search(r"0x[0-9A-Fa-f]+", answer)
                if hex_match:
                    OEL_OUT[0] = "SENSOR_ADDR = " + hex_match.group() + ";"

            case "Query: How do you initialize or reset the sensor? Include register addresses or command codes for initialization or soft reset or power-up.":
                hex_values = re.findall(r"0x[0-9A-Fa-f]+", answer)
                OEL_OUT[1] = "INIT_CMD = (" + ', '.join(hex_values) + ");" if hex_values else "INIT_CMD = ();"

            case "Query: What read command or register hexadecimal value triggers a sensor measurement? Which register address should be pointed to or read from to acquire data?":
                hex_values = re.findall(r"0x[0-9A-Fa-f]+", answer)
                OEL_OUT[2] = "READ_CMD = (" + ', '.join(hex_values) + ");" if hex_values else "READ_CMD = ();"

            case "Query: What is the sensor data output length in bytes?":
                int_match = re.search(r"\b\d+\b", answer)
                OEL_OUT[3] = f"DATA_LEN = {int_match.group()};" if int_match else "DATA_LEN = NaN;"

            case "Query: Where are the sensor measurement values stored in registers or memory? Include register addresses, byte ranges, or bit positions.":
                matches = re.findall(r"(\w+):\s*\[(\d+:\d+)\]", answer)
                if matches:
                    name_str = "(" + ", ".join(f'{i}: "{name}"' for i, (name, _) in enumerate(matches)) + ")"
                    range_str = "(" + ", ".join(f"{i}: [{rng}]" for i, (_, rng) in enumerate(matches)) + ")"
                    OEL_OUT[4] = "DATA_KEY_VAL = " + name_str + ";"
                    OEL_OUT[5] = "DATA_FORMAT = " + range_str + ";"
                else:
                    OEL_OUT[4] = "DATA_KEY_VAL = ();"
                    OEL_OUT[5] = "DATA_FORMAT = ();"

            case "Query: What is the formula or process for converting raw sensor output values to physical units like temperature, humidity, pressure, or altitude?":
                matches = re.findall(r"(\w+):\s*\"([^\"]+)\"", answer)
                if matches:
                    formula_str = "(" + ", ".join(f'{i}: "{formula}"' for i, (_, formula) in enumerate(matches)) + ")"
                    OEL_OUT[6] = "SCALE_FORMAT = " + formula_str + ";"
                else:
                    OEL_OUT[6] = "SCALE_FORMAT = ();"

    # Combine everything
    oel_code = f"NEW_SENSOR = {sensor_name};PROTOCOL = I2C;{OEL_OUT[0]}{OEL_OUT[1]}NEW_SENSOR_READ;{OEL_OUT[2]}{OEL_OUT[3]}{OEL_OUT[4]}{OEL_OUT[5]}{OEL_OUT[6]}"
    
    # Append to CSV rows
    csv_rows.append((file, oel_code))

# Sort rows by filename
csv_rows.sort(key=lambda row: row[0])

# Write to CSV
import time
csv_file_path = f"/home/steven/FYP/v2_LLM_OS/LLM/OEL_output/oel_output_{time.strftime('%Y-%m-%d-%H-%M-%S')}.csv"
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["txt_filename", "oel_code"])
    writer.writerows(csv_rows)

print(f"\n✅ OEL codes written to: {csv_file_path}")
