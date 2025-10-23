from transformers import pipeline
from transformers import AutoTokenizer
from transformers import AutoModel


checkpoint = "distilbert-base-uncased-finetuned-sst-2-english"
tokenizer = AutoTokenizer.from_pretrained(checkpoint)
model = AutoModel.from_pretrained(checkpoint)


raw_inputs = [
    "I've been waiting for a HuggingFace course my whole life.",
    "I hate this so much!",
]

# 第一步 tokenizer
inputs = tokenizer(raw_inputs, padding=True, truncation=True, return_tensors="pt")
print(inputs)

# 第二步 model
outputs = model(**inputs)
print(outputs.last_hidden_state.shape)
