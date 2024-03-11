import string
import random


def generate_email():
    username = 'ValentsinaPetukhova6'
    domain = 'yandex.ru'
    random_part = random.randint(100, 999)
    return f"{username}{random_part}@{domain}"


def generate_password():
    # Генерируем пароль
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(8))
    return password