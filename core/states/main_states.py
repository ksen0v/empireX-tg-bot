from aiogram.fsm.state import StatesGroup, State


class FormData(StatesGroup):
    name = State()
    age = State()
    country = State()
    experience = State()
    duration = State()
    schedule = State()
    payment = State()
    projects = State()
    wallet = State()
    email = State()
    device = State()


class Spam(StatesGroup):
    text = State()
