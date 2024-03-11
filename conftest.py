import pytest
from locators import *
from selenium.webdriver.common.by import By
from selenium import webdriver
from helpers import generate_email, generate_password


@pytest.fixture
def new_user_registration(driver):
    name = "Valentina"
    email = generate_email()
    password = generate_password()
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
def driver(request):
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")

    def fin():
        driver.quit()

    request.addfinalizer(fin)
    return driver
