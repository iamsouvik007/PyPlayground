# NLP Toolkit Application

A Python GUI application for natural language processing tasks including sentiment analysis, named entity recognition, and emotion detection using Google's Gemini API.

## Setup Instructions

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Environment Variables**
   - Create a `.env` file in the project root
   - Add your Gemini API key:
     ```
     GEMINI_API_KEY=your_actual_api_key_here
     ```
   - **Important**: Never commit your `.env` file to version control

3. **Run the Application**
   ```bash
   python app.py
   ```

## Features

- User registration and login system
- Sentiment analysis
- Named entity recognition
- Emotion detection
- Modern GUI with dark theme

## Security

- API keys are stored in environment variables
- The `.env` file is excluded from version control via `.gitignore`
- Never hardcode sensitive information in your source code
