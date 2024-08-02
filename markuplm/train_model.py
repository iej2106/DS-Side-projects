from transformers import MarkupLMForTokenClassification, Trainer, TrainingArguments
from datasets import load_from_disk

# Load dataset
dataset = load_from_disk('./tokenized_dataset')

# Load model
model = MarkupLMForTokenClassification.from_pretrained('microsoft/markuplm-base')

# Define training arguments
training_args = TrainingArguments(
    output_dir='./results',
    evaluation_strategy="epoch",
    per_device_train_batch_size=8,
    per_device_eval_batch_size=8,
    num_train_epochs=3,
    weight_decay=0.01,
)

# Initialize Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=dataset
)

# Train the model
trainer.train()
