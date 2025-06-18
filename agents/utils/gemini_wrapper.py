# import os
# from dotenv import load_dotenv
# import google.generativeai as genai

# load_dotenv()
# genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# model = genai.GenerativeModel('models/gemini-2.0-flash')

# def ask_gemini(prompt):
#     response = model.generate_content(prompt)
#     return response.text


import os
import time
import google.generativeai as genai
from dotenv import load_dotenv
from google.api_core.exceptions import ResourceExhausted

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel('models/gemini-2.0-flash')

def ask_gemini(prompt, max_retries=3):
    for attempt in range(max_retries):
        try:
            response = model.generate_content(prompt)
            return response.text
        except ResourceExhausted as e:
            print(f"⚠️ Quota exhausted on attempt {attempt + 1}. Retrying in 4 seconds...")
            time.sleep(4)  # wait before retrying
        except Exception as e:
            print(f"❌ Gemini API error: {e}")
            break
    return "⚠️ Gemini API error: Quota exceeded or too many requests. Try again later."
