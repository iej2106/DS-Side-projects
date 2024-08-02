from transformers import MarkupLMTokenizer
from datasets import Dataset

# Load the tokenizer
tokenizer = MarkupLMTokenizer.from_pretrained('microsoft/markuplm-base')

def tokenize_and_align_labels(texts, labels, xpaths, tokenizer):
    # Ensure xpaths is provided along with texts
    assert len(texts) == len(xpaths), "Number of texts and xpaths must match."
    
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

# Example data
texts = ["Employee Name: John Doe", "Pay Date: 01/16/2024"]
labels = [[1, 1, 0, 0, 0], [2, 2, 0, 0]]

# Example xpaths: Dummy values as placeholders, replace with actual xpaths
xpaths = [
    ["0", "1", "2", "3", "4"],
    ["0", "1", "2", "3"]
]

# Apply tokenization and label alignment
tokenized_data = tokenize_and_align_labels(texts, labels, xpaths, tokenizer)

print(tokenized_data)
