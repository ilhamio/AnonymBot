from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dispatcher, db


@dispatcher.message_handler(CommandStart())
async def bot_start(message: types.Message):
    chat_id = message.chat.id
    db.add_to_users(chat_id=chat_id)
    await message.answer(f"Привет, {message.from_user.full_name}!")
