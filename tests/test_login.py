from selenium.webdriver.common.by import By
from selenium import webdriver
from locators import *
import unittest
import string
import random


class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://stellarburgers.nomoreparties.site/")
        self.email = self.generate_email()
        self.password = self.generate_password()
        # Регистрируем нового пользователя перед каждым тестом
        self.register_new_user()

    def generate_email(self):
        username = 'ValentinaPetukhova6'
        domain = 'yandex.ru'
        random_part = random.randint(100, 999)
        return f"{username}{random_part}@{domain}"

    def generate_password(self):
        # Генерируем пароль
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(8))
        return password

    def register_new_user(self):
        name = "Valentina"
        self.driver.find_element(By.XPATH, LOGIN_ACCOUNT_BUTTON).click()
        self.driver.find_element(By.LINK_TEXT, REGISTER_LINK).click()
        self.driver.find_element(By.XPATH, NAME_REGISTRATION_INPUT).send_keys(name)
        self.driver.find_element(By.XPATH, EMAIL_REGISTRATION_INPUT).send_keys(self.email)
        self.driver.find_element(By.XPATH, PASSWORD_REGISTRATION_INPUT).send_keys(self.password)
        self.driver.find_element(By.XPATH, REGISTER_BUTTON).click()
        # Возвращаемся на главную страницу
        self.driver.get("https://stellarburgers.nomoreparties.site/")

    def test_login_using_button_on_the_main_page(self):
        # Нажимаем на кнопку Войти в аккаунт и вводим данные
        self.driver.find_element(By.XPATH, LOGIN_ACCOUNT_BUTTON).click()
        self.driver.find_element(By.CSS_SELECTOR, LOGIN_INPUT).send_keys(self.email)
        self.driver.find_element(By.CSS_SELECTOR, PASSWORD_INPUT).send_keys(self.password)
        self.driver.find_element(By.XPATH, LOGIN_BUTTON).click()
        # Проверяем, что после успешного входа произошел переход на главную страницу
        self.assertTrue(self.driver.find_element(By.CLASS_NAME, MAIN_PAGE).is_displayed())

    def test_login_using_personal_cabinet_button(self):
        # Нажимаем на кнопку Личный кабинет и вводим данные
        self.driver.find_element(By.XPATH, PERSONAL_ACCOUNT_BUTTON).click()
        self.driver.find_element(By.CSS_SELECTOR, LOGIN_INPUT).send_keys(self.email)
        self.driver.find_element(By.CSS_SELECTOR, PASSWORD_INPUT).send_keys(self.password)
        self.driver.find_element(By.XPATH, LOGIN_BUTTON).click()
        # Проверяем, что после успешного входа произошел переход на главную страницу
        self.assertTrue(self.driver.find_element(By.CLASS_NAME, MAIN_PAGE).is_displayed())

    def test_login_through_button_in_registration_form(self):
        # Переходим в форму регистрации, нажимаем кнопку Войти и вводим данные
        self.driver.find_element(By.XPATH, LOGIN_ACCOUNT_BUTTON).click()
        self.driver.find_element(By.LINK_TEXT, REGISTER_LINK).click()
        self.driver.find_element(By.LINK_TEXT, LOGIN_LINK).click()
        self.driver.find_element(By.CSS_SELECTOR, LOGIN_INPUT).send_keys(self.email)
        self.driver.find_element(By.CSS_SELECTOR, PASSWORD_INPUT).send_keys(self.password)
        self.driver.find_element(By.XPATH, LOGIN_BUTTON).click()
        # Проверяем, что после успешного входа произошел переход на главную страницу
        self.assertTrue(self.driver.find_element(By.CLASS_NAME, MAIN_PAGE).is_displayed())

    def test_login_through_button_recovery_button(self):
        # Переходим в форму авторизации, нажимаем кнопку восстановить пароль и вводим данные
        self.driver.find_element(By.XPATH, LOGIN_ACCOUNT_BUTTON).click()
        self.driver.find_element(By.LINK_TEXT, RECOVER_PASSWORD).click()
        self.driver.find_element(By.LINK_TEXT, LOGIN_LINK).click()
        self.driver.find_element(By.CSS_SELECTOR, LOGIN_INPUT).send_keys(self.email)
        self.driver.find_element(By.CSS_SELECTOR, PASSWORD_INPUT).send_keys(self.password)
        self.driver.find_element(By.XPATH, LOGIN_BUTTON).click()
        # Проверяем, что после успешного входа произошел переход на главную страницу
        self.assertTrue(self.driver.find_element(By.CLASS_NAME, MAIN_PAGE).is_displayed())

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()

