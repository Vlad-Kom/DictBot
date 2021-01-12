from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

help_but = InlineKeyboardMarkup(inline_keyboard=
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
    ]
]
                                             )