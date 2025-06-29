# my_api.py

import requests

class GeminiNLP:
    def __init__(self, api_key):
        self.api_key = api_key
        self.url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={self.api_key}"
        self.headers = {
            "Content-Type": "application/json"
        }

    def call_api(self, prompt):
        payload = {
            "contents": [
                {
                    "parts": [
                        {"text": prompt}
                    ]
                }
            ]
        }

        try:
            response = requests.post(self.url, headers=self.headers, json=payload)
            if response.status_code == 200:
                data = response.json()
                return data['candidates'][0]['content']['parts'][0]['text'].strip()
            else:
                return f"API Error {response.status_code}: {response.text}"
        except Exception as e:
            return f"Request failed: {str(e)}"

    def analyze_sentiment(self, text):
        prompt = f"""
        You are a sentiment analysis tool. Analyze the sentiment of the following text and respond with only one word: 
        Positive, Negative, or Neutral.\n\nText: {text}
        """
        return self.call_api(prompt)

    def analyze_ner(self, text):
        prompt = f"""
        You are an NLP tool. Extract all named entities from the following text and list them with their type (e.g., PERSON, LOCATION, ORGANIZATION).
        Return the result in this format: Entity - Type.\n\nText: {text}
        """
        return self.call_api(prompt)

    def analyze_emotion(self, text):
        prompt = f"""
        You are an emotion detection tool. Identify the main emotion in the following text and return one word: Joy, Sadness, Anger, Fear, Surprise, or Disgust.
        \n\nText: {text}
        """
        return self.call_api(prompt)
