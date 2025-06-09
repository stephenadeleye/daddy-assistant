import os
from dotenv import load_dotenv
import openai
from openai import OpenAIError

# Load environment variables once
load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")
if not API_KEY:
    raise RuntimeError("Missing OPENAI_API_KEY in environment")

# Initialize client once
client = openai.OpenAI(api_key=API_KEY)

# Constant system prompt
SYSTEM_PROMPT_TEMPLATE = (
    "You’re Daddy, a warm, wise Nigerian father and voice assistant. "
    "Respond to {user} in a personal and loving tone."
)

def process_input(prompt: str, user: str) -> str:
    """Send a user prompt and name to the assistant and return its reply."""
    try:
        resp = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT_TEMPLATE.format(user=user.title()),
                },
                {"role": "user", "content": prompt},
            ],
        )
        return resp.choices[0].message.content.strip()

    except OpenAIError as e:
        # More specific exception
        return f"Sorry, I encountered an API error: {e}"
    except Exception as e:
        # Fallback for anything else
        return f"Unexpected error: {e}"