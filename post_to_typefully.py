import requests

from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()
api_key = os.getenv("TYPEFULLY_API_KEY")
if not api_key:
    raise ValueError("TYPEFULLY_API_KEY not set in .env file.")

# Define the API endpoint
url = "https://api.typefully.com/v1/drafts/"

# Read the thread content from the file
with open("d:\\Cascade\\Qlik KT\\OE\\interactive_content\\threads\\2025-04-17_typefully_thread.txt", "r", encoding="utf-8") as file:
    content = file.read()

# Prepare the payload
payload = {
    "content": content,
    "threadify": True  # Automatically split content into tweets
}

# Set the headers
headers = {
    "X-API-KEY": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

# Make the POST request to create a draft
response = requests.post(url, json=payload, headers=headers)

# Check the response
if response.status_code == 200:
    print("Thread posted successfully!")
    print("Response:", response.json())
else:
    print("Failed to post thread.")
    print("Status Code:", response.status_code)
    print("Response:", response.text)
