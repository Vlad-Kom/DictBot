from random import shuffle
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def but_game(words):
    words = list(map(lambda x: x[0], words))
    shuffle(words)
    game = InlineKeyboardMarkup()
    for word in words:
        but = InlineKeyboardButton(text=word, callback_data=word)
        game.add(but)
    game.add(InlineKeyboardButton(text="Назад", callback_data="game"))
    return game