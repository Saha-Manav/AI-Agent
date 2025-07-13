import openai
import os
from openai import RateLimitError
from dotenv import load_dotenv

# Load environment variables from .env if available
load_dotenv()

# ✅ Set your API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# 🔄 Use mock summary in development/testing mode
USE_OPENAI = True

def summarize(text: str) -> str:
    if not USE_OPENAI:
        return "[Mock summary] This is a test summary of the user's reflection."

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

    except openai.AuthenticationError as e:
        return f" Invalid OpenAI API key: {e}"

    except Exception as e:
        return f" Unexpected error during summarization: {e}"
