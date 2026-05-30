import os
import base64
import requests
from dotenv import load_dotenv

load_dotenv()

endpoint = "https://smashraf110-8283-resource.services.ai.azure.com/providers/blackforestlabs/v1/flux-2-pro?api-version=preview"
api_key = os.getenv("AZURE_API_KEY")

prompt = input("Enter image prompt: ")

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

payload = {
    "prompt": prompt,
    "model": "FLUX.2-pro",
    "width": 1024,
    "height": 1024,
    "n": 1
}

response = requests.post(endpoint, headers=headers, json=payload)

if response.status_code != 200:
    print("Error:", response.status_code)
    print(response.text)
else:
    result = response.json()
    image_base64 = result["data"][0]["b64_json"]
    image_data = base64.b64decode(image_base64)

    with open("generated_image.png", "wb") as image_file:
        image_file.write(image_data)

    print("Image saved as generated_image.png")