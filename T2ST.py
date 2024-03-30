import torch, torchaudio
import yaml
import requests
import webbrowser
from gradio_client import Client

#### https://huggingface.co/spaces/facebook/seamless-m4t-v2-large

def run_inference(text):
    client = Client("https://facebook-seamless-m4t-v2-large.hf.space/--replicas/yj6v2/")
    result = client.predict(
            text,	# str  in 'Input text' Textbox component
            "English",	
            "Bengali",
            api_name="/t2st"
    )
    return result




    