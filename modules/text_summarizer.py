import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
if not GOOGLE_API_KEY:
    raise ValueError("Missing GOOGLE_API_KEY. Please check your .env file.")

genai.configure(api_key=GOOGLE_API_KEY)

# Use a lighter model for summarization
model = genai.GenerativeModel('gemini-1.5-flash')

def summarize_text(text):
    """Summarize the given text using Gemini API."""
    if not text:
        return {"error": "Text is required"}

    try:
        prompt = f"Summarize the following text concisely:\n\n{text}"
        response = model.generate_content(prompt)
        return {"summary": response.text}

    except Exception as e:
        return {"error": str(e)}
