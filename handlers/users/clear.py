from aiogram import types
from utils.db_api.sqlite import Database

from keyboards.inline.dict_buttons import dict_but
from keyboards.inline.language_clear_buttons import lang_clear_but
from states.dict import State_dict
from loader import dp


@dp.callback_query_handler(state=State_dict.dict_main, text="clear")
async def bot_delete(call: types.CallbackQuery):
    await call.message.edit_text('Какой словарь удалить?', reply_markup=lang_clear_but)
    await State_dict.dict_clear.set()

@dp.callback_query_handler(state=State_dict.dict_clear)
async def bot_state_delete(call: types.CallbackQuery):
    db = Database()
    if call.data == "en":
        data = "Английский"
    else:
        data = "Русский"
    db.delete_all_words(call.from_user.id, call.data)
    await call.message.edit_text(data + " словарь удален",  reply_markup=dict_but)
    await State_dict.dict_main.set()
