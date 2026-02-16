import google.generativeai as genai
from app.config import settings

genai.configure(api_key=settings.GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-2.0-flash")

async def generate_response(message: str, system_instruction: str = None) -> str:
    chat = model.start_chat(history=[])
    if system_instruction:
        chat.send_message(system_instruction)
    response = chat.send_message(message)
    return response.text
