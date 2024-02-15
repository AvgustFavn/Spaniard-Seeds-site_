import subprocess
from pathlib import Path

from django.test import TestCase

def send_data_new_order(data):
    BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
    # python_interpreter = f'{BASE_DIR}/venv/bin/python3.10'
    python_interpreter = f'{BASE_DIR}/venv/Scripts/python.exe'
    print(BASE_DIR)
    bot_script_path = f'{BASE_DIR}/seeds_shop/weed_proj/bot/new_order.py'
    print(python_interpreter, bot_script_path)
    argument_value = """🛍 У вас новый заказ! 🛍
    Email покупателя: a@a.com
    Имя покупателя: 8
    Контакты: тг - @aaaaaaaaaaa, номер - 222212
    Предпочтительная оплата: BTC
    Предпочтительная почта: Почта России
    Адрес: г. Москва, 8
    Товары:
    jjknjknjk - 1 шт.
    Полная сумма заказа: 20000.0
    """
    command = [python_interpreter, bot_script_path, argument_value]
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()

    # Вывод результатов
    print("Output:", output.decode())
    print("Error:", error.decode())

send_data_new_order('aaaaaa')