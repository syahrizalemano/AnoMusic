from config import API_HASH, API_ID, BOT_TOKEN, STRING
from pyrogram import Client

app = Client(
    "AnoMusic",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
)

userbot = Client(STRING, API_ID, API_HASH)
