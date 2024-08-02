import json
from datasets import Dataset
from transformers import MarkupLMTokenizer

# Load the JSON data
def load_from_json(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data

# Tokenization function
def tokenize_and_align_labels(texts, labels, xpaths, tokenizer):
    tokenized_inputs = tokenizer(texts, padding=True, truncation=True, return_offsets_mapping=True, xpaths=xpaths)
    
    aligned_labels = []
    
    for i, (offset_mapping, label) in enumerate(zip(tokenized_inputs['offset_mapping'], labels)):
        label_ids = [-100] * len(offset_mapping)
        
        for token_idx, (start, end) in enumerate(offset_mapping):
            if start == 0 and end == 0:
                label_ids[token_idx] = -100
            elif len(label) > token_idx:
                label_ids[token_idx] = label[token_idx]
        
        aligned_labels.append(label_ids)
    
    tokenized_inputs['labels'] = aligned_labels
    return tokenized_inputs

# Save to dataset
def save_to_dataset(tokenized_data, save_path='./tokenized_dataset'):
    train_dataset = Dataset.from_dict(tokenized_data)
    train_dataset.save_to_disk(save_path)
    print("Dataset saved to disk.")

# Load and process data
json_file_path = 'label_studio_export.json'
data = load_from_json(json_file_path)

# Extract texts, labels, and xpaths from JSON data
texts = [item['text'] for item in data]  # Adjust based on JSON structure
labels = [item['labels'] for item in data]  # Adjust based on JSON structure
xpaths = [item['xpaths'] for item in data]  # Adjust based on JSON structure

# Initialize tokenizer
tokenizer = MarkupLMTokenizer.from_pretrained('microsoft/markuplm-base')

# Tokenize data
tokenized_data = tokenize_and_align_labels(texts, labels, xpaths, tokenizer)

# Save tokenized data
save_to_dataset(tokenized_data)
