from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dispatcher


@dispatcher.message_handler(CommandHelp())
async def help_command(message: types.Message):
    text = (
        "Список команд:",
        "/start - команда запуска",
        "/help - информация о командах",
        "/search - поиск собеседника",
        "/stop - выйти из чата",
            )
    await message.answer('\n'.join(text))
