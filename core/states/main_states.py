from aiogram.fsm.state import StatesGroup, State

class BillStates(StatesGroup):
    amount = State()
    photo = State()

class Abstract(StatesGroup):
    temp = State()

class Calc(StatesGroup):
    calc1 = State()
    calc2 = State()
