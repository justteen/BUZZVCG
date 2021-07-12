import requests
from pyrogram import Client as Bot

from teamBUZZ.config import API_HASH
from teamBUZZ.config import API_ID
from teamBUZZ.config import BG_IMAGE
from teamBUZZ.config import BOT_TOKEN
from teamBUZZ.services.callsmusic import run

response = requests.get(BG_IMAGE)
file = open("./etc/foreground.png", "wb")
file.write(response.content)
file.close()

bot = Bot(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="teamBUZZ.modules"),
)

bot.start()
run()
