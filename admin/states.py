from aiogram.fsm.state import State,StatesGroup

class WaitMessage(StatesGroup):
    message1 = State()
    message2 = State()