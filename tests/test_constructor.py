from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *
import unittest
import string
import random


class ConstructorTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://stellarburgers.nomoreparties.site/")
        self.email = self.generate_email()
        self.password = self.generate_password()
        # Регистрируем нового пользователя перед каждым тестом
        self.register_new_user()

    def generate_email(self):
        username = 'ValentinePetukhova6'
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

    def test_switch_to_buns(self):
        # Login
        self.driver.find_element(By.XPATH, LOGIN_ACCOUNT_BUTTON).click()
        self.driver.find_element(By.CSS_SELECTOR, LOGIN_INPUT).send_keys(self.email)
        self.driver.find_element(By.CSS_SELECTOR, PASSWORD_INPUT).send_keys(self.password)
        self.driver.find_element(By.XPATH, LOGIN_BUTTON).click()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, BUNS_SECTION)))

        # Переключаемся на вкладку "Соусы", а затем возвращаемся на "Булки"
        sauces_element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, SAUCES_SECTION)))
        sauces_element.click()
        # Проверяем, что ранее скрытый элемент стал видимым
        element_sauce = self.driver.find_element(By.XPATH, SOME_SAUCE)
        self.assertTrue(element_sauce.is_displayed())

        buns_element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, BUNS_SECTION)))
        buns_element.click()

        # Проверяем, что ранее скрытый элемент стал видимым
        element_buns = self.driver.find_element(By.XPATH, SOME_BUNS)
        self.assertTrue(element_buns.is_displayed())

    def test_switch_to_sauces(self):
        # Login
        self.driver.find_element(By.XPATH, LOGIN_ACCOUNT_BUTTON).click()
        self.driver.find_element(By.CSS_SELECTOR, LOGIN_INPUT).send_keys(self.email)
        self.driver.find_element(By.CSS_SELECTOR, PASSWORD_INPUT).send_keys(self.password)
        self.driver.find_element(By.XPATH, LOGIN_BUTTON).click()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, SAUCES_SECTION)))

        # Переключаемся на вкладку "Соусы"
        sauces_element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, SAUCES_SECTION)))
        sauces_element.click()
        # Проверяем, что ранее скрытый элемент стал видимым
        element_sauce = self.driver.find_element(By.XPATH, SOME_SAUCE)
        self.assertTrue(element_sauce.is_displayed())

    def test_switch_to_fillings(self):
        # Login
        self.driver.find_element(By.XPATH, LOGIN_ACCOUNT_BUTTON).click()
        self.driver.find_element(By.CSS_SELECTOR, LOGIN_INPUT).send_keys(self.email)
        self.driver.find_element(By.CSS_SELECTOR, PASSWORD_INPUT).send_keys(self.password)
        self.driver.find_element(By.XPATH, LOGIN_BUTTON).click()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, FILLINGS_SECTION)))

        # Переключаемся на вкладку "Начинки"
        fillings_element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, FILLINGS_SECTION)))
        fillings_element.click()
        # Проверяем, что ранее скрытый элемент стал видимым
        element_filling = self.driver.find_element(By.XPATH, SOME_FILLING)
        self.assertTrue(element_filling.is_displayed())

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()