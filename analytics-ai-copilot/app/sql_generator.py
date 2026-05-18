from dotenv import load_dotenv
import os
import re
from groq import Groq

load_dotenv()  # garante leitura do .env

def get_client():
    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        raise ValueError("GROQ_API_KEY não encontrada. Verifique seu .env")

    return Groq(api_key=api_key)


def _extract_sql(text: str) -> str:
    # Strip all code fence markers regardless of position or variant
    cleaned = re.sub(r"```(?:sql)?", "", text, flags=re.IGNORECASE).strip()

    # Find the first SQL keyword
    match = re.search(r"(SELECT|INSERT|UPDATE|DELETE|WITH)\b", cleaned, re.IGNORECASE)
    if not match:
        return cleaned

    sql = cleaned[match.start():]

    # Trim everything after the first semicolon (end of statement)
    semi = sql.find(";")
    if semi != -1:
        sql = sql[: semi + 1]

    return sql.strip()


def generate_sql(question: str, schema: str):

    client = get_client()

    prompt = f"""Você é um especialista em SQLite. Responda SOMENTE com o SQL, sem explicações, sem markdown, sem texto adicional.
Use APENAS funções compatíveis com SQLite (ex: DATE('now'), strftime). Nunca use DATE_SUB, INTERVAL, ADD_MONTHS ou funções MySQL/PostgreSQL.

Schema:
{schema}

Pergunta: {question}

SQL:"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    raw = response.choices[0].message.content
    return _extract_sql(raw)