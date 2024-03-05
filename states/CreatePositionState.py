from aiogram.dispatcher.filters.state import State, StatesGroup


class CreatePositionState(StatesGroup):
    body = State()
    group = State()

