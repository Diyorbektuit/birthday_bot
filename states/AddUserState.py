from aiogram.dispatcher.filters.state import State, StatesGroup


class AddUserState(StatesGroup):
    body = State()
    position_id = State()
    tg_id = State()
    birthday = State()