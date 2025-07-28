import csv
from typing import List, Dict

def export_to_csv(data: List[Dict], filename: str):
    if not data:
        print("No data to export.")
        return
    with open(filename, "w", newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
