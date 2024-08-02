import json
import csv

# Input and Output file names
input_json_file = 'label_studio_export.json'
output_csv_file = 'paystub_data.csv'

# Load the JSON data
with open(input_json_file, 'r') as f:
    data = json.load(f)

# Prepare CSV file for writing
with open(output_csv_file, 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = [
        'id', 'text', 'file_upload'
    ]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    
    for entry in data:
        entry_id = entry.get('id', '')
        text = entry.get('data', {}).get('text', '')
        file_upload = entry.get('file_upload', '')

        writer.writerow({
            'id': entry_id,
            'text': text,
            'file_upload': file_upload
        })

print(f"Data successfully converted to {output_csv_file}")
