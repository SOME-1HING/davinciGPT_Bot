from DavinciGPT.config import *
from pyrogram import Client
from davinciGPT import Chatbot

chatbot = Chatbot("test")

app = Client("DavinciGPT", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
