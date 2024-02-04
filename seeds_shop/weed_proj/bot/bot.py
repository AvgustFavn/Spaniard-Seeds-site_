import json
import socket
import sys
from pathlib import Path

from aiogram.utils import executor

BASE_DIR = Path(__file__).resolve().parent.parent
import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
import psycopg2
try:
    from bot_back import session, User_tg
except:
    from bot.bot_back import session, User_tg

API_TOKEN = '6915120152:AAE6-oDuamRp8MMlMJ23FHfsXO81w9DwxfQ'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

async def start_bot_socket_listener():
    host = '127.0.0.1'  # Замените на ваш IP-адрес
    port = 8381  # Замените на порт, который вы указали для сокет-сервера

    bot_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    bot_socket.bind((host, port))
    bot_socket.listen()

    print(f"Бот слушает на порту {port}")

    while True:
        client_socket, addr = bot_socket.accept()
        data = client_socket.recv(1024).decode('utf-8')
        print(f"Получено сообщение от Django: {data}")
        data = data.replace("'", "\"")
        data = json.loads(data)
        if 'text_order' in data:
            text = data.get('text_order')
            await new_order(text)

        elif 'user' in data:
            email_value = data.get('user')
            await new_user(email_value)

        client_socket.close()

if __name__ == "__main__":
    start_bot_socket_listener()

# Обработчик команды /start
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    user_id = message.from_user.id
    user = session.query(User_tg).filter(User_tg.tg_id == user_id).first()
    if user == None:
        user = User_tg(tg_id=user_id, username=message.from_user.username)
        session.add(user)
        session.commit()
    await bot.send_message(text='Привет, удачной работы :)', chat_id=user_id)


async def new_user(email):
    text = f'👤 На вашем сайте зарегистрировался новый пользвоатель! 👤\n' \
           f'Почта: {email}'
    users = session.query(User_tg).all()
    print("новый юзер")
    for u in users:
        print(f'Теперь {u}')
        await bot.send_message(text=text, chat_id=u.tg_id)

async def new_order(text):
    users = session.query(User_tg).all()
    for u in users:
        await bot.send_message(text=text, chat_id=u.tg_id)



if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(start_bot_socket_listener())

    # Запуск бота Telegram
    executor.start_polling(dp, skip_updates=True)

