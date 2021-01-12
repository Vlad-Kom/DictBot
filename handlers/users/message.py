from aiogram import types

from keyboards.inline.start_buttons import start_but
from loader import dp


@dp.message_handler(state="*", content_types=types.ContentTypes.ANY)
async def bot_start_message(message: types.Message):
    await message.answer('Я вас не понимаю😕', reply_markup=start_but)
