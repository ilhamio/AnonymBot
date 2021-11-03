from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

search_callback = CallbackData("choice", "action")
button_1 = InlineKeyboardButton(text="Начать поиск", callback_data=search_callback.new(action="search"))
search_menu = InlineKeyboardMarkup(row_width=1, inline_keyboard=[[button_1]])

cancel_callback = CallbackData("choice", "action")
button_2 = InlineKeyboardButton(text="Остановить поиск", callback_data=cancel_callback.new(action="cancel"))
cancel_menu = InlineKeyboardMarkup(row_width=1, inline_keyboard=[[button_2]])