import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get API key
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

# Ensure API key is set correctly
if not GOOGLE_API_KEY:
    raise ValueError("Missing GOOGLE_API_KEY. Please check your .env file.")

# Configure API
genai.configure(api_key=GOOGLE_API_KEY)

# Select the correct model
model = genai.GenerativeModel("gemini-1.5-pro-latest")  # Change if needed

# Test generating content
try:
    response = model.generate_content("Explain quantum computing in simple terms.")
    print(response.text)
except Exception as e:
    print(f"Error: {e}")
