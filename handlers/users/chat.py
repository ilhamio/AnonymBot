from aiogram import types
from loader import dispatcher, db
from keyboards.inline.choice_keyboard import search_menu, search_callback, cancel_menu, cancel_callback


# Return inline-menu
@dispatcher.message_handler(commands=['search'])
async def start_chat(message: types.Message):
    text = "Для начала поиска нажмите на кнопку"
    if not db.find_value(message.chat.id, 'queue'):
        await message.answer(text, reply_markup=search_menu)
    else:
        await message.answer("[BOT]: Вы уже начали поиск собеседника!")


# handler for start searching
@dispatcher.callback_query_handler(search_callback.filter(action="search"))
async def search_callback(cbq: types.CallbackQuery):
    await cbq.answer()
    if db.add_to_queue(cbq.message.chat.id):
        await cbq.message.edit_reply_markup(None)
        await cbq.message.edit_text("<b>Собеседник найден!</b>")
    else:
        await cbq.message.edit_reply_markup(cancel_menu)


# handler for cancel searching
@dispatcher.callback_query_handler(cancel_callback.filter(action="cancel"))
async def cancel_callback(cbq: types.CallbackQuery):
    await cbq.answer()
    db.delete_from_queue(cbq.message.chat.id)
    await cbq.message.edit_reply_markup(None)
    await cbq.message.edit_text("<b>Здесь ничего не было!</b>")


@dispatcher.message_handler()
async def chat(message: types.Message):
    companion = db.get_companion(message.chat.id)
    if companion:
        await dispatcher.bot.send_message(companion, message.text)


@dispatcher.message_handler(commands=['stop'])
async def stop_chat(message: types.Message):
    chat_id = message.chat.id
    companion = db.get_companion(chat_id)

    db.close_chat(chat_id)
    db.close_chat(companion)

    await message.answer("Вот и все!")
    await dispatcher.bot.send_message(companion, "Вот и все!")