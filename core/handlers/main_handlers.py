from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, FSInputFile
from aiogram import Bot

from config_loader import MESSAGES, LINK_RAR, ADMIN_ID
from ..keyboards.inline.inline_keyboards import *
from ..states.main_states import FormData, Spam
from ..db import *

async def get_start(message: Message, state: FSMContext):
    await state.clear()
    #await message.answer(MESSAGES['start'], reply_markup=start_inline())
    await add_user(message.from_user.id)
    photo = FSInputFile('media/meme.webp')  # Replace with your photo filename in root folder
    await message.answer_photo(photo, caption=str(MESSAGES['start']).format(name=message.from_user.username), reply_markup=start_inline())


async def get_promo(callback_query: CallbackQuery):
    await callback_query.message.answer(MESSAGES['promo'], reply_markup=promo_inline())
    await callback_query.answer()


async def promo_yes(callback_query: CallbackQuery):
    await callback_query.message.answer(MESSAGES['promo_yes'], reply_markup=promo_yes_inline())
    await callback_query.answer()


async def promo_no(callback_query: CallbackQuery):
    await callback_query.message.answer(MESSAGES['promo_no'], reply_markup=promo_yes_inline())
    await callback_query.answer()


async def get_name(callback_query: CallbackQuery, state: FSMContext):
    await callback_query.message.answer(MESSAGES['get_name'])
    await state.set_state(FormData.name)
    await callback_query.answer()


async def get_age(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer(MESSAGES['get_age'])
    await state.set_state(FormData.age)


async def get_country(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.answer(MESSAGES['get_country'])
    await state.set_state(FormData.country)


async def get_expirience(message: Message, state: FSMContext):
    await state.update_data(country=message.text)
    await message.answer(MESSAGES['get_expirience'])
    await state.set_state(FormData.experience)


async def get_duration(message: Message, state: FSMContext):
    await state.update_data(experience=message.text)
    await message.answer(MESSAGES['get_duration'])
    await state.set_state(FormData.duration)


async def get_schedule(message: Message, state: FSMContext):
    await state.update_data(duration=message.text)
    await message.answer(MESSAGES['get_schedule'])
    await state.set_state(FormData.schedule)


async def get_payment(message: Message, state: FSMContext):
    await state.update_data(schedule=message.text)
    await message.answer(MESSAGES['get_payment'])
    await state.set_state(FormData.payment) 


async def get_projects(message: Message, state: FSMContext):
    await state.update_data(payment=message.text)
    await message.answer(MESSAGES['get_projects'])
    await state.set_state(FormData.projects)


async def get_wallet(message: Message, state: FSMContext):
    await state.update_data(projects=message.text)
    await message.answer(MESSAGES['get_wallet'])
    await state.set_state(FormData.wallet)


async def get_email(message: Message, state: FSMContext):
    await state.update_data(wallet=message.text)
    await message.answer(MESSAGES['get_email'])
    await state.set_state(FormData.email)


async def get_device(message: Message, state: FSMContext):
    await state.update_data(email=message.text)
    await message.answer(MESSAGES['get_device'])
    await state.set_state(FormData.device)


async def form(message: Message, state: FSMContext):
    await state.update_data(device=message.text)
    data = await state.get_data()

    await message.answer(str(MESSAGES['form']).format(name=data['name'],
                                                      age=data['age'],
                                                      country=data['country'],
                                                      experience=data['experience'],
                                                      duration=data['duration'],
                                                      schedule=data['schedule'],
                                                      payment=data['payment'],
                                                      projects=data['projects'],
                                                      wallet=data['wallet'],
                                                      email=data['email'],
                                                      device=data['device']), 
                        reply_markup=send_or_fix_inline())
    await state.clear()


async def send_rar(callback_query: CallbackQuery):
    await callback_query.message.answer(str(MESSAGES['send_rar']).format(link=LINK_RAR),
                                        reply_markup=download_or_no_inline())
    await callback_query.answer()


async def download_yes(callback_query: CallbackQuery):
    await callback_query.message.answer(MESSAGES['download_yes'], 
                                        reply_markup=your_choose_inline())
    await callback_query.answer()


async def download_no(callback_query: CallbackQuery):
    await callback_query.message.answer(MESSAGES['download_no'])
    await callback_query.answer()


async def super(callback_query: CallbackQuery):
    await callback_query.message.answer(MESSAGES['super'],
                                        reply_markup=send_post_or_manager_inline())
    await callback_query.answer()


async def notification_after_5_days(bot: Bot):
    users = await get_notification_user()

    if users:
        for user in users:
            user_id = user[0]
            try:
                await bot.send_message(user_id, MESSAGES['notification_after_5_days'])
                await set_next_notification(user_id)
            except Exception as e:
                logger.info(e)


async def spam(message: Message, state: FSMContext):
    await message.answer('Рассылка\n\nЧтобы написать имя пользователя, то в тексте напиши {name}\n\nНапишите текст для рассылки:')
    await state.set_state(Spam.text)


async def spam_start(message: Message, state: FSMContext):
    await state.update_data(text=message.text)
    data = await state.get_data()
    text = data['text']
    user_ids = await get_all_users()
    user_ids_no_admin = [uid for uid in user_ids if uid != ADMIN_ID]

    if user_ids_no_admin:
        count = 1
        for i, user_id in enumerate(user_ids_no_admin):
            try:
                chat = await message.bot.get_chat(user_id)
                username = chat.username

                await message.bot.send_message(user_id, str(text).format(name=username))

                logger.info(f'Рассылка {i} - Успешно отправлено пользователю {user_id}')
                count += 1
            except Exception as e:
                logger.info(f'Рассылка {i} - Не удалось отправить пользователю {user_id}: {e}')
        await message.answer(f'Рассылка закончена, отправлено: {count}/{len(user_ids_no_admin)}')
    else:
        await message.answer(f'База данных пуста.')