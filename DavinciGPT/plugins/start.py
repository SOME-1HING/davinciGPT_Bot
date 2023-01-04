from pyrogram import filters
from pyrogram.types import Message
from DavinciGPT import app


@app.on_message(filters.command("start"))
async def start_cmd(_, message: Message):
    await message.reply_text(
        """
Hello, I am DavinciGPT, an advance AI bot that uses ChatGPT davinci model. 

ChatGPT davinci is a natural language processing (NLP) chatbot powered by OpenAI's GPT-3 language model. It is designed to provide users with an AI-powered conversational experience that can understand and respond to natural language queries. ChatGPT davinci can be used for customer service, virtual assistants, and more. It is capable of understanding complex conversations and providing accurate responses in real-time.

Integration done by @SOME1HING
"""
    )
