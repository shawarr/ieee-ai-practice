from transformers import pipeline
generator = pipeline("text-generation", model="gpt2")

result = generator("tell me a joke", max_length=100)

print(result[0]['generated_text'])