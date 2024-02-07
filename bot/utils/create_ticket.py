from aiogram.fsm.state import State, StatesGroup


class Form(StatesGroup):
    title = State()
    description = State()
    