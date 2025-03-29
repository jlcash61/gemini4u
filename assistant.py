# assistant.py
import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

class GeminiAssistant:
    def __init__(self, model="gemini-1.5-flash"):
        self.api_key = os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY not found in .env file.")
        self.model = model
        self.endpoint = f"https://generativelanguage.googleapis.com/v1beta/models/{self.model}:generateContent?key={self.api_key}"
        self.headers = {"Content-Type": "application/json"}

    def ask(self, prompt):
        payload = {
            "contents": [
                {
                    "parts": [{"text": prompt}]
                }
            ]
        }

        try:
            response = requests.post(self.endpoint, headers=self.headers, data=json.dumps(payload))
            if response.ok:
                result = response.json()
                return result['candidates'][0]['content']['parts'][0]['text']
            else:
                return f"[HTTP Error {response.status_code}]: {response.text}"
        except Exception as e:
            return f"[Exception]: {e}"
