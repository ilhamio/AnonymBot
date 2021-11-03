from aiogram import Dispatcher, Bot, types
from data.config import BOT_TOKEN
from database import db_api

db = db_api.Database('bot2.db')

bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)
dispatcher = Dispatcher(bot=bot)
