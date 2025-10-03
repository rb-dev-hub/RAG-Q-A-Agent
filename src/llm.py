from openai import OpenAI
from dotenv import load_dotenv
import os

def set_key():
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    client= OpenAI()
    return client

def get_llm_response(prompt, context, client):
    message = [
    { "role": "system", 
      "content": "You are a helpful assistant, always answering to the point. If you do not know something, just say it. Do not make stuff up." 
    },
    {"role": "user", 
      "content": f"User Query: {prompt}\n\nUser the following information to answer the user's question(s): {context}"
    }
    ]
    response = client.responses.create(
    model="gpt-4.1-nano",
    input=message
    )
    return response.output_text

def ask_ai(prompt, context):
    client =set_key()
    return get_llm_response(prompt, context, client)
