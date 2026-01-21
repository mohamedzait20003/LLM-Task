import os
from google import genai
from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv()

# Get API key from environment variable
api_key = os.getenv('GOOGLE_API_KEY')
if not api_key:
    raise ValueError("GOOGLE_API_KEY not found in .env file")

client = genai.Client(api_key=api_key)

def generate_llama_opinion(prompt):
    response = client.models.generate_content(
        model="gemini-2.0-flash-lite",
        contents=prompt,
        config={
            "temperature": 0.8,
            "max_output_tokens": 100
        }
    )
    
    return response.text

prompt = input("Enter your prompt: ")
print(generate_llama_opinion(prompt))