from aiogram import types
from utils.db_api.sqlite import Database

from keyboards.inline.back_dict_button import back_dict_but
from states.dict import State_dict
from loader import dp


@dp.callback_query_handler(state=State_dict.dict_main, text="delete")
async def bot_delete(call: types.CallbackQuery):
    await call.message.edit_text('Какое слово удалить?', reply_markup=back_dict_but)
    await State_dict.dict_delete.set()


@dp.message_handler(state=State_dict.dict_delete)
async def bot_state_delete(message: types.Message):
    db = Database()
    if db.check_word(id=message.chat.id, word=message.text) is None:
        await message.answer('Такого слова нет в словарях 😢\n'
                             'Попробуйте другое слово', reply_markup=back_dict_but)
    else:
        await message.answer('Отлично! \n'
                     'Слово "' + message.text + '" удалено из словаря')
        db.delete_word(id=message.chat.id, word=message.text)
