#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 9583161
API_HASH = "aecf9e2b7c655c4f916564ab6d598a73" 
BOT_TOKEN = "6283547148:AAFQDyUEzjCnf4QXBPdwfQUJzlrAxE_h5_U" 
SESSION = "BACSOjkAsMNa24WFWjNinqk3NZvBR2wu2fkJnwGDpLHX5RjWqmIy1m_ULtRewFA-EtnIqpJf5rS5JEyL9GpJfRzg4EOfx5eBF4KTChhdYaP_89YwGjzPdiEXVXp8WfHHYypBXr2U4Sz9Req8cJ8uhvuyFCg9tYYJl1C8OUNfZaNTtbJomYsMMPppreVeuamuqaWgLNbnZHzKFQfQzIL4O17_K7Hk01kMs4G_Af_P2wrBqmE5sGIr4Zkck4IFCRNpkQE-HLHX6fRoiFkVSuri9SQlW4_XumtDBWqTR36_DsI54svntdJz3SJeV3hFr5N6o4EHNl3Wt6QUkgqSHHFXso7WOCnbMQAAAAFkDKwgAA"
FORCESUB = "Xargbot" 
AUTH = 5973519392

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client(
    session_name=SESSION, 
    api_hash=API_HASH, 
    api_id=API_ID)

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
