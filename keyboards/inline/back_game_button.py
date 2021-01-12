from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

back_game_but = InlineKeyboardMarkup(inline_keyboard=
[
    [
        InlineKeyboardButton(
            text="Словарь",
            callback_data="dict"
        )
    ],
    [
        InlineKeyboardButton(
            text="Назад",
            callback_data="game"
        )
    ]
]
                                             )
