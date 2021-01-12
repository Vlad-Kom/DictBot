from aiogram import types
from aiogram.dispatcher.storage import FSMContext
from utils.db_api.sqlite import Database
from states.game import State_game
from keyboards.inline.game_buttons import but_game
from keyboards.inline.back_game_button import back_game_but
from keyboards.inline.language_game_buttons import lang_game_but
from utils.func import game_translate_word
from random import choice

from loader import dp

db = Database()


@dp.callback_query_handler(state="*", text="game")
async def bot_dict(call: types.CallbackQuery):
    await call.message.edit_text("Нужно выбрать словарь для игры", reply_markup=lang_game_but)
    await State_game.game_main.set()


@dp.callback_query_handler(state=State_game.game_main)
async def bot_game_main(call: types.CallbackQuery, state: FSMContext):
    words = db.set_words(call.message.chat.id, call.data)
    if not words:
        return await call.message.edit_text("В словаре слишком мало слов для игры 😢 \n"
                                          "Что будем делать?\n",
                                 reply_markup=back_game_but)
    await state.update_data(
        {
            "language": call.data,
            "answer": words[0][0]
        }
    )
    await call.message.edit_text("Перевод какого это слова?\n" + game_translate_word(words[0][0]),
                                 reply_markup=but_game(words))
    await State_game.game_answer.set()


@dp.callback_query_handler(state=State_game.game_answer)
async def bot_game_answer(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    lst_answer = ['Правильно! \n',
                  'Да, верно!\n',
                  'Безупречно!\n',
                  '+ очко!\n',
                  'Блестяще!\n'
                  ]
    answer = data.get("answer")
    words = db.set_words(call.message.chat.id, data.get("language"))
    await state.update_data(answer=words[0][0])
    if call.data == answer:
        db.increase_value_word(call.message.chat.id, answer)
        await call.message.edit_text(choice(lst_answer) + 'Продолжаем👇🏻\n' + game_translate_word(words[0][0]),
                                     reply_markup=but_game(words))
    else:
        db.zero_value_word(call.message.chat.id, answer)
        await call.message.edit_text('Неверно😢\n'
                                     'Правильный ответ - ' + answer + '\n'
                                                                      'Продолжаем👇🏻\n' + game_translate_word(words[0][0]),
                                     reply_markup=but_game(words))
