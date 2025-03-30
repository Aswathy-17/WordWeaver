import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
if not GOOGLE_API_KEY:
    raise ValueError("Missing GOOGLE_API_KEY. Please check your .env file.")

genai.configure(api_key=GOOGLE_API_KEY)

# Use correct model name
model = genai.GenerativeModel('gemini-1.5-pro-latest')

def generate_content(topic):
    """Generate content about a given topic using Gemini API."""
    if not topic:
        return {"error": "Topic is required"}

    try:
        prompt = f"Write a well-structured, informative, and engaging article about {topic}."
        response = model.generate_content(prompt)
        return {"content": response.text}

    except Exception as e:
        return {"error": str(e)}
