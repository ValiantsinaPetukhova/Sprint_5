import pytest
import string
import random
from locators import *
from selenium.webdriver.common.by import By
from selenium import webdriver


@pytest.fixture
def generate_email():
    username = 'ValentsinaPetukhova6'
    domain = 'yandex.ru'
    random_part = random.randint(100, 999)
    return f"{username}{random_part}@{domain}"


@pytest.fixture
def generate_password():
    # Генерируем пароль
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(8))
    return password


@pytest.fixture
def new_user_registration(driver_creation, generate_email, generate_password):
    name = "Valentina"
    email = generate_email
    password = generate_password
    driver = driver_creation
    driver.find_element(By.XPATH, LOGIN_ACCOUNT_BUTTON).click()
    driver.find_element(By.LINK_TEXT, REGISTER_LINK).click()
    driver.find_element(By.XPATH, NAME_REGISTRATION_INPUT).send_keys(name)
    driver.find_element(By.XPATH, EMAIL_REGISTRATION_INPUT).send_keys(email)
    driver.find_element(By.XPATH, PASSWORD_REGISTRATION_INPUT).send_keys(password)
    driver.find_element(By.XPATH, REGISTER_BUTTON).click()
    # Возвращаемся на главную страницу
    driver.get("https://stellarburgers.nomoreparties.site/")
    return email, password


@pytest.fixture
def driver_creation():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    return driver
