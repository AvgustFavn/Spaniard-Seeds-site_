# -*- coding: utf-8 -*-
import asyncio
import logging
import os
import sys
import time
from pathlib import Path

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.types import ParseMode, Update
from aiogram.utils import executor

# BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
# python_path = "venv/Scripts/python.exe"
# os.environ['PATH'] = f"{BASE_DIR}/{python_path}:{os.environ['PATH']}"

from bot_back import User_tg, session

API_TOKEN = '6915120152:AAE6-oDuamRp8MMlMJ23FHfsXO81w9DwxfQ'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

async def main(somwthing):
    text = f'{somwthing}'
    users = session.query(User_tg).all()
    for u in users:
        await bot.send_message(text=text, chat_id=u.tg_id)
    await bot.close()

if __name__ == '__main__':
    text = sys.argv[1]
    print(text, type(text))
    executor.start_polling(dp, on_startup=lambda dp: asyncio.create_task(main(text)))
