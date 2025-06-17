import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel('models/gemini-2.0-flash')

def ask_gemini(prompt):
    response = model.generate_content(prompt)
    return response.text
