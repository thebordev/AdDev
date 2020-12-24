import logging
from aiogram import Bot, Dispatcher

from settings import BOT_TOKEN

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)