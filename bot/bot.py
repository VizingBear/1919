import asyncio

from aiogram import Bot, Dispatcher, types, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart

from config import TOKEN
from .handlers import *
from .keyboards import *


bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()
# dp.include_routers()

@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer("Приветственное сообщение", reply_markup=base_keyboard)
