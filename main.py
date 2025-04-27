from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()

generator = pipeline('text-generation', model="gpt2")

class UserInput(BaseModel):
    prompt: str

@app.post('/generate_text')
def generate_text(input: UserInput):
    output= generator(input.prompt, max_length=50, num_return_sequences=1)

    generated_text = output[0]['generated_text']

    return{'generated_text': generated_text}