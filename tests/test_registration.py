from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import *
import unittest
import string
import random


class RegistrationTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://stellarburgers.nomoreparties.site/")
        self.email = self.generate_email()
        self.password = self.generate_password()

    def generate_email(self):
        username = 'ValentinaPetuhova6'
        domain = 'yandex.ru'
        random_part = random.randint(100, 999)
        return f"{username}{random_part}@{domain}"

    def generate_password(self):
        # Генерируем пароль
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(8))
        return password

    def test_successful_registration(self):
        name = "Valentina"
        self.driver.find_element(By.XPATH, LOGIN_ACCOUNT_BUTTON).click()
        self.driver.find_element(By.LINK_TEXT, REGISTER_LINK).click()
        self.driver.find_element(By.XPATH, NAME_REGISTRATION_INPUT).send_keys(name)
        self.driver.find_element(By.XPATH, EMAIL_REGISTRATION_INPUT).send_keys(self.email)
        self.driver.find_element(By.XPATH, PASSWORD_REGISTRATION_INPUT).send_keys(self.password)
        self.driver.find_element(By.XPATH, REGISTER_BUTTON).click()
        WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, LOGIN_PAGE)))

        # Проверяем успешную регистрацию, пробуем ввести логин и пароль
        self.driver.find_element(By.CSS_SELECTOR, LOGIN_INPUT).send_keys(self.email)
        self.driver.find_element(By.CSS_SELECTOR, PASSWORD_INPUT).send_keys(self.password)
        # Проверяем, что после успешного входа произошел переход на главную страницу
        self.assertTrue(self.driver.find_element(By.CLASS_NAME, MAIN_PAGE).is_displayed())

    def test_registration_with_invalid_password(self):
        # Данные для регистрации
        name = "Valentina"
        invalid_password = "short"

        # Переход на страницу регистрации ввод данных
        self.driver.find_element(By.XPATH, LOGIN_ACCOUNT_BUTTON).click()
        self.driver.find_element(By.LINK_TEXT, REGISTER_LINK).click()
        self.driver.find_element(By.XPATH, NAME_REGISTRATION_INPUT).send_keys(name)
        self.driver.find_element(By.XPATH, EMAIL_REGISTRATION_INPUT).send_keys(self.email)
        self.driver.find_element(By.XPATH, PASSWORD_REGISTRATION_INPUT).send_keys(invalid_password)
        self.driver.find_element(By.XPATH, REGISTER_BUTTON).click()

        # Проверяем наличие сообщения об ошибке
        error_message = self.driver.find_element(By.CSS_SELECTOR, ERROR_MESSAGE_PASSWORD)
        self.assertTrue(error_message.is_displayed())

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()

