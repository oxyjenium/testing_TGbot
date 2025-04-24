from aiogram.fsm.state import State, StatesGroup

class Information(StatesGroup):
    name = State()
    age = State()
    click = State()
    