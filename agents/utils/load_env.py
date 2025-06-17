from dotenv import load_dotenv
import os

def load_env_key():
    load_dotenv()
    return os.getenv("GEMINI_API_KEY")