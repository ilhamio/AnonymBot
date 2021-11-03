from aiogram import executor
from utils.notification import start_notification
import handlers
from loader import dispatcher


if __name__ == '__main__':
    executor.start_polling(dispatcher=dispatcher, on_startup=start_notification)
