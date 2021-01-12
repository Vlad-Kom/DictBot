from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

start_but = InlineKeyboardMarkup(inline_keyboard=
[
    [
        InlineKeyboardButton(
            text="Словарь",
            callback_data="dict"
        )
    ],
    [
        InlineKeyboardButton(
            text="Игра",
            callback_data="game"
        )
    ],
    [
        InlineKeyboardButton(
            text="Помощь",
            callback_data="help"
        )
    ]
]
                                             )
