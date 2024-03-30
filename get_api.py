import requests
from bs4 import BeautifulSoup
import json
import re

def get_endpoint():

    # URL of the webpage you want to scrape
    url = 'https://facebook-seamless-m4t-v2-large.hf.space/?view=api'

    # Send a GET request to the webpage
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page with BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all <script> tags in the HTML
        script_tags = soup.find_all('script')

        # Define a pattern to match the desired URL structure within the script content
        pattern = re.compile(r'"root":"(https://facebook-seamless-m4t-v2-large\.hf\.space/--replicas/([^"]+))"')

        # Search each script tag for the pattern
        for script in script_tags:
            if script.string:  # Only proceed if the script tag contains text
                match = pattern.search(script.string)
                if match:
                    # Extract the entire URL and the specific portion
                    full_url = match.group(1)
                    specific_portion = match.group(2)
                    return full_url
    else:
        print(f"Failed to fetch the SeamlessM4T. Status code: {response.status_code}")
