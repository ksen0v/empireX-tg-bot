from aiogram.utils.keyboard import InlineKeyboardBuilder
from config_loader import MESSAGES

def top_up_by_card_inline():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text='💰 Банковской картой', callback_data='top_up_by_card')
    keyboard.adjust(1)

    return keyboard.as_markup()

def popup_inline():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text='💳 Пополнить', callback_data='top_up_by_card_two')
    keyboard.adjust(1)

    return keyboard.as_markup()

def contact_support_inline():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text='✉️ Связаться', callback_data='contact_support')
    keyboard.adjust(1)

    return keyboard.as_markup()

def main_menu_inline():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text='🏠 Главное меню', callback_data='main_menu')
    keyboard.adjust(1)

    return keyboard.as_markup()

def news_inline():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text='📰 Перейти в новостник', url=str(MESSAGES['link_to_news_for_keyboard']))
    keyboard.adjust(1)

    return keyboard.as_markup()

def reviews_inline():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text='😄 Отзывы', url=str(MESSAGES['link_to_reviews_for_keyboard']))
    keyboard.adjust(1)

    return keyboard.as_markup()