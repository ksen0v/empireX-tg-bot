from aiogram.types import Message
from aiogram import Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import FSInputFile, CallbackQuery, ContentType
import random

from config_loader import MESSAGES
from keyboards.reply.reply_keyboards import start_menu_reply


async def get_start(message: Message, state: FSMContext):
    await state.clear()
    photo = FSInputFile('media/start_photo.jpg')  # Replace with your photo filename in root folder
    await message.answer_photo(photo, caption=MESSAGES['startup_user'], reply_markup=start_menu_reply())


