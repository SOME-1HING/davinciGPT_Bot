import asyncio
import importlib
from pyrogram import idle
from DavinciGPT.plugins import ALL_MODULES
from DavinciGPT import app
from DavinciGPT.logger import LOGGER

loop = asyncio.get_event_loop()


async def init():
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("DavinciGPT.plugins" + all_module)
    LOGGER.info("Successfully Imported Modules ")


if __name__ == "__main__":
    loop.run_until_complete(init())
    LOGGER.info("Stopping DavinciGPT! GoodBye")
