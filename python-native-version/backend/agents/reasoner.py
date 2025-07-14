import openai
from openai import RateLimitError

def reason(summary):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Analyze and suggest root causes and next steps."},
                {"role": "user", "content": summary}
            ]
        )
        return response['choices'][0]['message']['content'].strip()
    except RateLimitError:
        return " API quota exceeded. Please check your OpenAI plan."
    except Exception as e:
        return f" Reasoning failed: {e}"
