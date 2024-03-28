from openai import OpenAI
import os
import yaml

def load_api_key():
    with open("secrets.yaml", "r") as file:
        secrets = yaml.safe_load(file)
    return secrets 

secrets = load_api_key()
huggingface_api_key = secrets["huggingface"]["HF_TOKEN"]
openai_api_key = secrets["openai"]["OPENAI_API_KEY"]


os.environ["OPENAI_API_KEY"] = openai_api_key
client = OpenAI()

def get_response(query):
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": query}],
        temperature=0.1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    reply = response.choices[0].message.content
    return reply