import openai
import os
from openai import RateLimitError

# ✅ Set your API key (ensure it's available in your environment variables)
openai.api_key = os.getenv("OPENAI_API_KEY")

# 🔄 Toggle this to False to use mock summary during development/testing
USE_OPENAI = True

def summarize(text: str) -> str:
    if not USE_OPENAI:
        return " [Mock summary] This is a test summary of the user's reflection."

    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Summarize the following user reflection."},
                {"role": "user", "content": text}
            ]
        )
        return response.choices[0].message.content.strip()
    
    except RateLimitError:
        return " API quota exceeded. Please check your OpenAI billing and limits."
    
    except Exception as e:
        return f" Unexpected error during summarization: {e}"
