import os
import socket
import subprocess
import time
from pathlib import Path

from django import forms
from django.contrib.sessions.models import Session

from bot.bot import BASE_DIR
from weed_site.models import Admins, Category


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)




def send_data_new_user(data):
    BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
    python_interpreter = f'{BASE_DIR}/venv/bin/python3.10'
    # python_interpreter = f'{BASE_DIR}/venv/Scripts/python.exe'
    print(BASE_DIR)
    bot_script_path = f'{BASE_DIR}/seeds_shop/weed_proj/bot/new_user.py'
    print(python_interpreter, bot_script_path)
    argument_value = data
    command = [python_interpreter, bot_script_path, argument_value]
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

def send_data_new_order(data):
    BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
    python_interpreter = f'{BASE_DIR}/venv/bin/python3.10'
    # python_interpreter = f'{BASE_DIR}/venv/Scripts/python.exe'
    print(BASE_DIR)
    bot_script_path = f'{BASE_DIR}/seeds_shop/weed_proj/bot/new_order.py'
    print(python_interpreter, bot_script_path)
    argument_value = data.encode('utf-8')
    command = [python_interpreter, bot_script_path, argument_value]
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    try:
        decoded_output = output.decode('utf-8')
        print("Output:", decoded_output)
    except UnicodeDecodeError:
        print("Unable to decode using UTF-8. Trying with a different encoding...")
        decoded_output = output.decode('latin-1')  # You can try other encodings as well
        print("Output:", decoded_output)

    try:
        decoded_output = error.decode('utf-8')
        print("error:", decoded_output)
    except UnicodeDecodeError:
        print("Unable to decode using UTF-8. Trying with a different encoding...")
        decoded_output = error.decode('latin-1')  # You can try other encodings as well
        print("error:", decoded_output)


def insert_values():
    Category.objects.create(name='Автоцветущие')
    Category.objects.create(name='Фотопериодные')
    Category.objects.create(name='Сатива')
    Category.objects.create(name='Индика')
    Category.objects.create(name='Медицинские')
    Category.objects.create(name='Для новичков')
    Category.objects.create(name='Невысокие')
    Category.objects.create(name='Слабопахнущие')

def handle_uploaded_file(uploaded_file, destination_folder):
    # Генерируем уникальное имя файла
    file_name = uploaded_file.name

    # Собираем путь для сохранения файла
    destination_path = os.path.join(destination_folder, file_name)

    # Открываем файл и сохраняем его
    with open(destination_path, 'wb') as destination_file:
        for chunk in uploaded_file.chunks():
            destination_file.write(chunk)

    # Возвращаем имя сохраненного файла
    return file_name


def get_user_id_from_session(session_id):
    try:
        # Получение объекта сессии по id сессии
        session = Session.objects.get(session_key=session_id)

        # Получение данных сессии (в формате JSON)
        session_data = session.get_decoded()

        # Получение id пользователя из данных сессии
        user_id = session_data.get('_auth_user_id')

        # Если пользователь найден, возвращаем его id
        if user_id:
            return user_id
        else:
            return None

    except:
        return None

def is_admin(user_id):
    adm = Admins.objects.filter(user_id=user_id).first()
    if adm:
        return True
    else:
        return False
