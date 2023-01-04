import asyncio
import importlib
from pyrogram import idle
from DavinciGPT.plugins import ALL_MODULES
from DavinciGPT import app
from DavinciGPT.logger import LOGGER
from DavinciGPT.config import LOG_GROUP_ID

from DavinciGPT.plugins.start import start_cmd

loop = asyncio.get_event_loop()


async def init():
    LOGGER.info("DavinciGPT is starting.")
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("DavinciGPT.plugins" + all_module)
    LOGGER.info("Successfully Imported Modules ")
    try:
        await app.send_message(LOG_GROUP_ID, "DavinciGPT Started.")
    except:
        LOGGER.error("Bot wasn't able to send message in the log group.")

    LOGGER.info("DavinciGPT started.")
    await idle()


if __name__ == "__main__":
    loop.run_until_complete(init())
    LOGGER.info("DavinciGPT Stopped.")
    loop.close()
    print("Bot Stopped")
