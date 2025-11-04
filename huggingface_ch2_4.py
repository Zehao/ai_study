from transformers import BertTokenizer

tokenizer = BertTokenizer.from_pretrained("bert-base-cased")

res1 = tokenizer("Using a Transformer network is simple")

res2 = tokenizer.tokenize("Using a Transformer network is simple")
ids = tokenizer.convert_tokens_to_ids(res2)

tokenizer.decode(ids)

# tokenizer.save_pretrained("/Users/bytedance/llm/data")
