from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

lang_game_but = InlineKeyboardMarkup(inline_keyboard=
[
    [
        InlineKeyboardButton(
            text="Русский",
            callback_data="ru"
        )
    ],
    [
        InlineKeyboardButton(
            text="Английский",
            callback_data="en"
        )
    ],
    [
        InlineKeyboardButton(
            text="Назад",
            callback_data="start"
        )
    ]
]
                                             )
