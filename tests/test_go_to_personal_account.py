from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import *
import unittest
import string
import random


class SwitchToAccountTest(unittest.TestCase):
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

    def test_going_on_personal_account_page(self):
        # Login
        self.driver.find_element(By.XPATH, LOGIN_ACCOUNT_BUTTON).click()
        self.driver.find_element(By.CSS_SELECTOR, LOGIN_INPUT).send_keys(self.email)
        self.driver.find_element(By.CSS_SELECTOR, PASSWORD_INPUT).send_keys(self.password)
        self.driver.find_element(By.XPATH, LOGIN_BUTTON).click()
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located((By.CLASS_NAME, MAIN_PAGE)))
        # Переходим в личный кабинет
        self.driver.find_element(By.XPATH, PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(self.driver, 4).until(
            expected_conditions.visibility_of_element_located((By.LINK_TEXT, PROFILE_PAGE)))
        account_page = self.driver.find_element(By.LINK_TEXT, PROFILE_PAGE)
        # Проверяем, что отображается страница личного кабинета
        self.assertTrue(account_page.is_displayed())

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()

