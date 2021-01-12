from aiogram import types

from states.start import State_start
from keyboards.inline.help_buttons import help_but
from loader import dp

@dp.callback_query_handler(state=State_start.start, text = "help")
async def bot_help(call: types.CallbackQuery):
    text = [
        'Cловарь - сборник слов, перевод которых вы хотите знать',
        '🔘 Удалить слово - удаление указанного слова из словаря',
        '🔘 Очистить словарь - очищает словарь\n',
        'Игра - игра, в которой вам дается перевод и 4 варианта ответа, Вам нужно верно назвать слово/фразу. У каждого слова/фразы есть счетчик, при 10 безошибочных ответов, оно удаляется из словаря'
    ]
    await call.message.edit_text('\n'.join(text), reply_markup=help_but)
