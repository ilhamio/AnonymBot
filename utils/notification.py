import logging
from aiogram import Dispatcher
from data.config import ADMINS


async def start_notification(dispatcher: Dispatcher) -> None:
    for admin in ADMINS:
        try:
            await dispatcher.bot.send_message(admin, "Бот запущен, Милорд!")
        except Exception as err:
            logging.log(err)
