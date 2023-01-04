from pyrogram import filters
from pyrogram.types import Message
from DavinciGPT import app, chatbot


@app.on_message(filters.text & filters.private)
async def chatbot_res(_, message: Message):
    query = message.text
    res = await chatbot.chatbot(query)
    return await message.reply_text(res)
