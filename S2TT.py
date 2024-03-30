import torch, torchaudio
import yaml
import requests
from gradio_client import Client

#### https://huggingface.co/spaces/facebook/seamless-m4t-v2-large

def run_inference(file_path, api_endpoint):
    #client = Client("https://facebook-seamless-m4t-v2-large.hf.space/--replicas/yj6v2/")
    client = Client(api_endpoint)
    result = client.predict(
            file_path,	# filepath  in 'Input speech' Audio component
            "Bengali",	
            "English",
            api_name="/s2tt")
    return result




    