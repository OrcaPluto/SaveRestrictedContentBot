#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 22535766
API_HASH = "ebb6fec4dcf17596adfb0c04a05d20ea"
BOT_TOKEN = "6193291147:AAFvKyTuWMWtw-n5HQvwh71oXifXPXMCy5I"
SESSION = "AQFX3lYAKFCTiSaGq6CmFKVhbwCIB2aBwffgqzYMy1VudIgoIjrM-Ne_vodUtCbLcDu4vPzk8qX_J7RJbVY9W9e0c6LIPFvNIm064XygolrWULf4kfERq1eJxHMQ2HFls704pOcsLdQh6gcoQYrhgPPnGxHbavIdX_Gya6w08IJ7gjsMEXjBe4_bc13VZeTm1YCT5IXapnrb8bqm0ROG45wBP9UCNFxm8MhpR6eShgw7VdWVPy4RZQAa2S43mKYxSXlcJ51OS5aEBvBewfZn7c7CoSjKf72Y2DEbk6xOqyQqd-pA__-S8-nITNEGC4hnZ3CCBCjdBKp8Ueo16x2DNVBc2HjQlQAAAAFiZi0aAA"
FORCESUB = "SaveRSC"
AUTH = "5945830682"

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
