import os

HEADERS = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {os.environ['OPENAI_API_KEY']}",
    "OpenAI-Beta": "assistants=v1"
}

HEADERS_OLD = {
    "Authorization: Bearer ": f"Bearer {os.environ['OPENAI_API_KEY']}",
}