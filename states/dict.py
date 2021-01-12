from aiogram.dispatcher.filters.state import StatesGroup, State

class State_dict(StatesGroup):
    dict_main = State()
    dict_translate = State()
    dict_delete = State()
    dict_clear = State()
