import logging

# enable logging
FORMAT = "[DavinciGPT] %(message)s"
logging.basicConfig(
    handlers=[logging.FileHandler("bot_logs.txt"), logging.StreamHandler()],
    level=logging.INFO,
    format=FORMAT,
    datefmt="[%X]",
)
logging.getLogger("pyrogram").setLevel(logging.INFO)
logging.getLogger("ptbcontrib.postgres_persistence.postgrespersistence").setLevel(
    logging.WARNING
)

LOGGER = logging.getLogger("[DavinciGPT]")
LOGGER.info("DavinciGPT is starting. | Built by SOME1HING. | Licensed under GPLv3.")
LOGGER.info("Handled by: github.com/SOME-1HING (t.me/SOME1HING)")
