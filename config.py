import os
import logging
from logging.handlers import RotatingFileHandler




BOT_TOKEN = os.environ.get("BOT_TOKEN", "7728674789:AAFs4f1A7K2pFP-LbhTE0Zq3ZSNa9dZh0Vw")
API_ID = int(os.environ.get("API_ID", "26069929"))
API_HASH = os.environ.get("API_HASH", "b0551dd4dd9e81b47fe6aa92173aff24")


OWNER_ID = int(os.environ.get("OWNER_ID", "6586630448"))
DB_URL = os.environ.get("DB_URL", "mongodb+srv://Luefvt:6369@rename.jjkcm.mongodb.net/?retryWrites=true&w=majority&appName=Rename")
DB_NAME = os.environ.get("DB_NAME", "Rename")


CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002369130075"))
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002189440226"))


FILE_AUTO_DELETE = int(os.getenv("FILE_AUTO_DELETE", "600")) # auto delete in seconds


PORT = os.environ.get("PORT", "8080")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))



try:
    ADMINS=[6586630448]
    for x in (os.environ.get("ADMINS", "6586630448").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")









CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

DISABLE_CHANNEL_BUTTON = True if os.environ.get('DISABLE_CHANNEL_BUTTON', "True") == "True" else False

BOT_STATS_TEXT = "<b>BOT UPTIME :</b>\n{uptime}"







USER_REPLY_TEXT = "<b> ❌Don't Send Me Messages Directly I'm Only File Share Bot ! </b>"

START_MSG = os.environ.get("START_MESSAGE", " <b> Hello {first}.I Can Store Private Files In Specified Channel And Other Users Can Access It From Special Link. </b>")

FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {mention}\n\n<b>You Need To Join In My Channel/Group To Use Me\n\nKindly Please Join Channel</b>")





ADMINS.append(OWNER_ID)
ADMINS.append(6586630448)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
   





# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Backup Channel @JishuBotz
# Developer @JishuDeveloper
