from aiogram import types

from keyboards.inline.back_dict_button import back_dict_but
from utils.func import translate_word
from states.dict import State_dict
from loader import dp


@dp.callback_query_handler(state=State_dict.dict_main, text="translate")
async def bot_translate(call: types.CallbackQuery):
    await call.message.edit_text('Что перевести?', reply_markup=back_dict_but)
    await State_dict.dict_translate.set()


@dp.message_handler(state=State_dict.dict_translate)
async def bot_state_translate(message: types.Message):
    try:
        result = translate_word(id_user=message.chat.id, word=message.text.lower())
        if result == 0:
            await message.answer("Не могу перевести😢\n "
                                 "Возможно, вы используете цифры или эмодзи",
                             reply_markup=back_dict_but)
            return
        if result == 1:
            await message.answer('Слишком много слов для меня😅 \n'
                                 'Давай что-нибудь попроще. Не больше трех слов',
                             reply_markup=back_dict_but)
            return
        if result == 2:
            await message.answer("Не могу перевести😢\n "
                                          "Проверьте текст, что-то с ним не так...",
                             reply_markup=back_dict_but)
            return
        await message.answer(result,
                         reply_markup=back_dict_but)
    except:
        await message.answer(message.chat.id, 'Что-то пошло не так',
                         reply_markup=back_dict_but)