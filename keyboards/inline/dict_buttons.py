from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

dict_but = InlineKeyboardMarkup(inline_keyboard=
[
    [
        InlineKeyboardButton(
            text="Заполнить словарь",
            callback_data="translate"
        )
    ],
    [
        InlineKeyboardButton(
            text="Удалить слово",
            callback_data="delete"
        )
    ],
    [
        InlineKeyboardButton(
            text="Очистить словарь",
            callback_data="clear"
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