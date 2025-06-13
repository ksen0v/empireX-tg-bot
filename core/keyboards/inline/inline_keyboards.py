from aiogram.utils.keyboard import InlineKeyboardBuilder


def start_inline():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text='🔥 Да, хочу попробовать!', callback_data='start_callback')
    keyboard.adjust(1)

    return keyboard.as_markup()


def promo_inline():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text='✅ Да, готов участвовать!', callback_data='promo_yes_callback')
    keyboard.button(text='🤔 Есть вопросы', callback_data='promo_no_callback')
    keyboard.adjust(1)

    return keyboard.as_markup()


def promo_yes_inline():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text='📝 Заполнить анкету', callback_data='fill_form_callback')
    keyboard.adjust(1)

    return keyboard.as_markup()


def send_or_fix_inline():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text='✅ Да, отправить', callback_data='send_form_callback')
    keyboard.button(text='✏️ Исправить', callback_data='fill_form_callback')
    keyboard.adjust(1)

    return keyboard.as_markup()


def download_or_no_inline():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text='📥 Скачал, пробую', callback_data='download_yes_callback')
    keyboard.button(text='🆘 Не открывается', callback_data='download_no_callback')
    keyboard.adjust(1)

    return keyboard.as_markup()


def your_choose_inline():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text='💵 Фиксированная оплата', callback_data='super')
    keyboard.button(text='📊 % с продаж', callback_data='super')
    keyboard.button(text='🎙️ Обсудить в голосовом', callback_data='super')
    keyboard.adjust(1)

    return keyboard.as_markup()


def send_post_or_manager_inline():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text='📌 Отправить ссылку на пост', callback_data='zero')
    keyboard.button(text='💬 Связаться с менеджером  @empireXmanager', url='t.me/empireXmanager')
    keyboard.adjust(1)

    return keyboard.as_markup()
