from aiogram import Dispatcher, F
from aiogram.filters import Command
import asyncio

from core.handlers.main_handlers import *
from config_loader import TOKEN, ADMIN_ID, MESSAGES
from core.states.main_states import FormData

from core.logger import logger
from core.db import init_db

from core.filters.admin_check import IsAdmin


async def startup_bot(bot: Bot):
    asyncio.create_task(task_notification(bot))
    try:
        await bot.send_message(ADMIN_ID, MESSAGES['startup_admin'])
        logger.info(f'Сообщение о запуске успешно отправлено админу - {ADMIN_ID}')
    except Exception as e:
        logger.error(f'Не удалось отправить сообщение о запуске админу - {ADMIN_ID}. Ошибка: {e}')


async def task_notification(bot: Bot):
    while True:
        await notification_after_5_days(bot)
        logger.info("Notif. check is done!")
        await asyncio.sleep(300)


async def main():
    bot = Bot(TOKEN, parse_mode='HTML')
    dp = Dispatcher()

    dp.startup.register(startup_bot)

    #HANDLERS
    dp.message.register(get_start, F.text == '/start')
    dp.callback_query.register(get_promo, F.data == 'start_callback' )
    dp.callback_query.register(promo_yes, F.data == 'promo_yes_callback')
    dp.callback_query.register(promo_no, F.data == 'promo_no_callback')

    #FORM FILL HANDLERS (STATES)
    dp.callback_query.register(get_name, F.data == 'fill_form_callback')
    dp.message.register(get_age, FormData.name)
    dp.message.register(get_country, FormData.age)
    dp.message.register(get_expirience, FormData.country)
    dp.message.register(get_duration, FormData.experience)
    dp.message.register(get_schedule, FormData.duration)
    dp.message.register(get_payment, FormData.schedule)
    dp.message.register(get_projects, FormData.payment)
    dp.message.register(get_wallet, FormData.projects)
    dp.message.register(get_email, FormData.wallet)
    dp.message.register(get_device, FormData.email)
    dp.message.register(form, FormData.device)

    # OUTPUT FORM
    dp.callback_query.register(form, FormData.payment)
    
    dp.callback_query.register(send_rar, F.data == 'send_form_callback')
    dp.callback_query.register(download_yes, F.data == 'download_yes_callback')
    dp.callback_query.register(download_no, F.data == 'download_no_callback')
    dp.callback_query.register(super, F.data == 'super')

    # ADMIN HANDLERS
    dp.message.register(spam, Command('spam'), IsAdmin)
    dp.message.register(spam_start, Spam.text)

    await init_db()

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(main())
