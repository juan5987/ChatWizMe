import os
import openai
from dotenv import load_dotenv

load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY')
openai.api_key = SECRET_KEY


def call_api(userMsg):
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=f"Correct this to standard English:{userMsg}",
        temperature=0,
        max_tokens=60,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
        )
    
    return response['choices'][0]['text']