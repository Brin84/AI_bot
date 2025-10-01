from aiogram.fsm.state import State, StatesGroup


class Creator(StatesGroup):
    wait = State()