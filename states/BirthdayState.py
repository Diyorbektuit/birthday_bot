from aiogram.dispatcher.filters.state import State, StatesGroup


class BirthdayState(StatesGroup):
    body = State()
