from aiogram.dispatcher.filters.state import State, StatesGroup


class CreateGroupState(StatesGroup):
    body = State()
