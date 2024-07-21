# Created By hakutakaid
import logging
from pyrogram import Client, filters
import pyotp
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv(".env")

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Get environment variables
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Initialize the Client
HAKU = Client(
    name="haku",
    api_id=int(API_ID),
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@HAKU.on_message(filters.command("start"))
async def welcome(client, message):
    logger.info(f"Received /start command from {message.from_user.id}")
    await message.reply("<b>Send Your 2FA</b>")

@HAKU.on_message(filters.text)
async def get_otp(client, message):
    kode = message.text
    logger.info(f"Received OTP key from {message.from_user.id}: {kode}")
    try:
        totp = pyotp.TOTP(kode)
        sekarang = totp.now()
        await message.reply(f"<b>Current OTP : </b><code>{sekarang}</code>")
        logger.info(f"Sent OTP to {message.from_user.id}: {sekarang}")
    except Exception as e:
        await message.reply(str(e))
        logger.error(f"Error while generating OTP for {message.from_user.id}: {str(e)}")

logger.info("Starting HAKU bot")
HAKU.run()