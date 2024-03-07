from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import *
import unittest
import string
import random


class SwitchFromAccountTest(unittest.TestCase):
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

    def test_switch_from_personal_account_to_constructor(self):
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
        # Переходим к конструктор
        self.driver.find_element(By.XPATH, CONSTRUCTOR_BUTTON).click()
        constructor_page = self.driver.find_element(By.CLASS_NAME, CONSTRUCTOR_PAGE)
        # Проверяем, что отображается страница с конструктором
        self.assertTrue(constructor_page.is_displayed())

    def test_click_from_personal_to_logo(self):
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
        # Нажимаем на логотип
        self.driver.find_element(By.CSS_SELECTOR, LOGO_AREA).click()
        main_page = self.driver.find_element(By.CLASS_NAME, MAIN_PAGE)
        # Проверяем, что отображается главная страница
        self.assertTrue(main_page.is_displayed())

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()

