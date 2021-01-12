from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.inline.start_buttons import start_but
from states.start import State_start
from utils.db_api.sqlite import Database
from loader import dp

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer('Для того чтобы узнать перевод слова/фразы выберите "Словарь"', reply_markup=start_but)
    db = Database()
    if db.check_user(id=message.chat.id) is None:
        db.add_user(id=message.chat.id, name=message.from_user.full_name)
    await State_start.start.set()

@dp.callback_query_handler(state="*", text = "start")
async def bot_start(call: types.CallbackQuery):
    await call.message.edit_text('Вернулись в начало \n'
                                 'Что будем делать?', reply_markup=start_but)
    await State_start.start.set()
