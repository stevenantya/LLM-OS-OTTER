import os
import re
import csv

def extract_helpful_chunks(folder_path, output_csv="v2_helpful_chunks_results.csv"):
    pattern = re.compile(r"Number of helpful chunks:\s*(\d+)")

    rows = []

    for filename in sorted(os.listdir(folder_path)):
        if filename.endswith(".txt"):
            with open(os.path.join(folder_path, filename), 'r', encoding='utf-8') as f:
                content = f.read()

            matches = pattern.findall(content)

            # Ensure exactly 6 values (pad with None if fewer)
            chunk_values = [int(x) for x in matches[:6]] + [None] * (6 - len(matches))

            row = {"Filename": filename}
            for i in range(6):
                row[f"Helpful Chunk {i+1}"] = chunk_values[i]

            rows.append(row)

    headers = ["Filename"] + [f"Helpful Chunk {i+1}" for i in range(6)]

    with open(output_csv, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows)

    print(f"[✓] Helpful chunks results saved to: {output_csv}")

extract_helpful_chunks("/home/steven/FYP/v2_LLM_OS/LLM/experiment_logs")