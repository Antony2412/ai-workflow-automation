import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def summarize_ticket(text: str) -> str:
    """
    Generate a concise enterprise-friendly summary of a support ticket.
    Falls back gracefully if LLM is unavailable.
    """
    if not client.api_key:
        return text[:100] + "..." if len(text) > 100 else text

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "system",
                "content": "You summarize enterprise support tickets in one concise sentence."
            },
            {
                "role": "user",
                "content": text
            }
        ],
        temperature=0.2
    )

    return response.choices[0].message.content.strip()
