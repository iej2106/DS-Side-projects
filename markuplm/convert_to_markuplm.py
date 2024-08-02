import json

def convert_label_studio_to_markuplm(input_file, output_file):
    with open(input_file, 'r') as f:
        data = json.load(f)
    
    converted_data = []
    for item in data:
        text = item.get('text', '')
        entities = []
        for annotation in item.get('annotations', []):
            for entity in annotation.get('result', []):
                # Adjust based on the actual structure of your Label Studio export
                entities.append({
                    "start": entity.get('from', 0),
                    "end": entity.get('to', 0),
                    "label": entity.get('value', '')
                })
        
        converted_data.append({
            "text": text,
            "entities": entities
        })
    
    with open(output_file, 'w') as f:
        json.dump(converted_data, f, indent=2)

if __name__ == "__main__":
    input_file = 'label_studio_export.json'  # Input file from Label Studio
    output_file = 'markuplm_data.json'       # Output file for MarkupLM
    convert_label_studio_to_markuplm(input_file, output_file)
    print(f"Converted data saved to {output_file}")
