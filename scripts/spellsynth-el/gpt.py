# gpt.py
# Text completions using OpenAI's API
# (https://platform.openai.com/docs/api-reference)

# ----- IMPORTS ----- #

from dotenv import load_dotenv
import os
import openai

load_dotenv()
client = openai.OpenAI(api_key = os.getenv('OPENAI_API_KEY'))

# ----- INFERENCE ----- #

# complete()
# Takes prompt and system_prompt strings, calls specified model, returns a string
def complete(prompt: str, **kwargs):
        
    messages = [
            {"role": "system", "content": 'You output JSON in the following format: {"el":"", "en":""}.'},
            {"role": "user", "content": prompt} 
    ]
    
    try:
        response = client.chat.completions.create(
            model = "gpt-4-1106-preview",
            messages = messages,
            response_format={ "type": "json_object" },
            timeout = 250,
            **kwargs
        )
        return response.choices[0].message.content
    
    except Exception as exception:
        print(exception)
        return None