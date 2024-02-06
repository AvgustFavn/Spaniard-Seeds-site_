import os
import socket
import time

from django import forms
from django.contrib.sessions.models import Session

from weed_site.models import Admins, Category


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

def send_data_to_socket(data):
    host = '127.0.0.1'
    port = 8381

    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host, port))
        client_socket.send(data.encode('utf-8'))

        # Флушим буфер
        client_socket.shutdown(socket.SHUT_WR)

    except Exception as e:
        print(f"Ошибка при отправке данных: {e}")

    finally:
        client_socket.close()

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
