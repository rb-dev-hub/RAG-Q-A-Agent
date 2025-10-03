
from openai import OpenAI
from dotenv import load_dotenv
import os

def set_key():
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    client= OpenAI()
    return client

def embed(input_text, client):
    response = client.embeddings.create(
        input=input_text,
        model="text-embedding-3-small",
        #dimensions=256
    )
    return response.data[0].embedding

def get_embedding(input_text):
    client =set_key()
    return embed(input_text, client)