from aiogram import types
from states.dict import State_dict

from keyboards.inline.dict_buttons import dict_but

from loader import dp


@dp.callback_query_handler(state="*", text="dict")
async def bot_dict(call: types.CallbackQuery):
    await call.message.edit_text('Для того чтобы узнать перевод слова/фразы выберите "Заполнить словарь"', reply_markup=dict_but)
    await State_dict.dict_main.set()