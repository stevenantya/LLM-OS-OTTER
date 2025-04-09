import os
import re
import csv

def extract_latencies_by_column(folder_path, output_csv="v2_structured_latency_results.csv"):
    # List of labels (without "Latency for" prefix)
    labels = [
        "What is the I2C address hexadecimal value?",
        "How do you initialize or reset the sensor? Include register addresses or command codes for initialization or soft reset or power-up.",
        "What read command or register hexadecimal value triggers a sensor measurement? Which register address should be pointed to or read from to acquire data?",
        "What is the sensor data output length in bytes?",
        "Where are the sensor measurement values stored in registers or memory? Include register addresses, byte ranges, or bit positions.",
        "What is the formula or process for converting raw sensor output values to physical units like temperature, humidity, pressure, or altitude?"
    ]

    # Regex patterns
    section_pattern = re.compile(
        r"Latency for (.*?):\s+"
        r"retrieve_chunk: ([\d.]+) seconds\s+"
        r"validate_chunk: ([\d.]+) seconds\s+"
        r"function: ([\d.]+) seconds",
        re.DOTALL
    )
    e2e_pattern = re.compile(r"Latency:\s*([\d.]+)\s*seconds")

    # List to hold rows
    rows = []

    for filename in sorted(os.listdir(folder_path)):
        if filename.endswith(".txt"):
            with open(os.path.join(folder_path, filename), "r", encoding="utf-8") as f:
                content = f.read()

            row = {"Filename": filename}

            # Initialize row keys for each label and metric
            for label in labels:
                for metric in ["retrieve_chunk", "validate_chunk", "function"]:
                    key = f"Latency for {label} {metric}"
                    row[key] = None

            # Extract and fill latency values
            for match in section_pattern.findall(content):
                label, retrieve, validate, function = match
                label = label.strip()
                if label in labels:
                    row[f"Latency for {label} retrieve_chunk"] = float(retrieve)
                    row[f"Latency for {label} validate_chunk"] = float(validate)
                    row[f"Latency for {label} function"] = float(function)

            # Match end-to-end latency
            e2e_match = e2e_pattern.search(content)
            row["end_to_end_latency"] = float(e2e_match.group(1)) if e2e_match else None

            rows.append(row)

    # Generate CSV headers
    headers = ["Filename"]
    for label in labels:
        for metric in ["retrieve_chunk", "validate_chunk", "function"]:
            headers.append(f"Latency for {label} {metric}")
    headers.append("end_to_end_latency")

    # Write to CSV
    with open(output_csv, "w", newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows)

    print(f"[✓] Structured latency results saved to: {output_csv}")

# Example usage
extract_latencies_by_column("/home/steven/FYP/v2_LLM_OS/LLM/experiment_logs")
