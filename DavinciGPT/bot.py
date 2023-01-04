from config import *
from pyrogram import Client, filters
from logger import LOGGER
import sys


class Bot:
    def __init__(self):
        self.bot = Client(
            "DavinciGPT", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN
        )

    async def start(self):
        LOGGER.info("DavinciGPT is starting.")

        await self.bot.start()

        try:
            await self.bot.send_message(LOG_GROUP_ID, "Assistant Started")
        except:
            LOGGER.error("Bot wasn't able to send message in the log group/")
            sys.exit()

        LOGGER.info("DavinciGPT started.")
