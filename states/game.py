from aiogram.dispatcher.filters.state import StatesGroup, State

class State_game(StatesGroup):
    game_lang = State()
    game_main = State()
    game_answer = State()
