import os

from openai import OpenAI
from dotenv import load_dotenv


# Carrega variáveis do .env
load_dotenv()


# API Key
api_key = os.getenv("OPENROUTER_API_KEY")


# Cliente OpenRouter
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key
)


def ask_ai(system_prompt, user_message):

    try:

        response = client.chat.completions.create(
            model="meta-llama/llama-3.1-8b-instruct",

            temperature=0.4,

            messages=[
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": user_message
                }
            ]
        )

        return response.choices[0].message.content

    except Exception as erro:

        return f"""
ERRO DE COMUNICAÇÃO COM A IA

Detalhes:
{erro}

Verifique:
- conexão com internet
- API Key
- créditos do OpenRouter
- disponibilidade do modelo
"""