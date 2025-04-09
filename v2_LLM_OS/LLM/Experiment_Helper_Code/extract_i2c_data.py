import os
import re
import csv

def extract_latencies_from_folder(folder_path, output_csv="v2_latency_results.csv"):
    # Define the regex patterns to extract latency values
    patterns = {
        "Datasheet fetch latency": r"Datasheet fetch latency:\s*([\d.]+)\s*seconds",
        "Datasheet partition latency": r"Datasheet partition latency:\s*([\d.]+)\s*seconds",
        "Vector DB embedding latency": r"Vector DB embedding latency:\s*([\d.]+)\s*seconds"
    }

    data = []

    # Sort filenames lexicographically
    for filename in sorted(os.listdir(folder_path)):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                row = {"Filename": filename}
                for label, pattern in patterns.items():
                    match = re.search(pattern, content)
                    row[label] = float(match.group(1)) if match else None
                data.append(row)

    # Define CSV headers
    headers = ["Filename"] + list(patterns.keys())

    # Write to CSV
    with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)

    print(f"[✓] Latency results saved to: {output_csv}")

# Example usage:
extract_latencies_from_folder("/home/steven/FYP/v2_LLM_OS/LLM/experiment_logs")
