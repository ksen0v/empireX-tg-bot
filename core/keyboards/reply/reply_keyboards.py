from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def start_menu_reply():
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text='💰 Пополнить'),
                KeyboardButton(text='🍪 Купить робуксы'),
                KeyboardButton(text='🍪 Вывод')
            ],
            [
                KeyboardButton(text='🧑‍💻 Поддержка'),
                KeyboardButton(text='👤 Профиль'),
                KeyboardButton(text='💹 Курс')
            ],
            [
                KeyboardButton(text='📰 Новостник'),
                KeyboardButton(text='😀 Отзывы')
            ],
            [
                KeyboardButton(text='🔢 Калькулятор')
            ]
        ],
        resize_keyboard=True,
        one_time_keyboard=False
    )
    return keyboard

def back_menu_reply():
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text='🏠 Главное меню')
            ]
        ],
        resize_keyboard=True,
        one_time_keyboard=False
    )
    return keyboard

def calc_reply():
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text='🌟 Посчтитать рубли в RBX'),
                KeyboardButton(text='🌟 Посчитать RBX в рубли')
            ],
            [
                KeyboardButton(text='🏠 Главное меню')
            ]
        ],
        resize_keyboard=True,
        one_time_keyboard=False
    )
    return keyboard