from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *


class TestConstructor:
    def test_switch_to_buns(self, driver):
        # Переключаемся на вкладку "Соусы", а затем возвращаемся на "Булки"
        sauces_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, SAUCES_SECTION)))
        sauces_element.click()
        # Проверяем, что ранее скрытый элемент стал видимым
        element_sauce = driver.find_element(By.XPATH, SOME_SAUCE)
        assert element_sauce.is_displayed()

        buns_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, BUNS_SECTION)))
        buns_element.click()

        # Проверяем, что ранее скрытый элемент стал видимым
        element_buns = driver.find_element(By.XPATH, SOME_BUNS)
        assert element_buns.is_displayed()

    def test_switch_to_sauces(self, driver):

        # Переключаемся на вкладку "Соусы"
        sauces_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, SAUCES_SECTION)))
        sauces_element.click()
        # Проверяем, что ранее скрытый элемент стал видимым
        element_sauce = driver.find_element(By.XPATH, SOME_SAUCE)
        assert element_sauce.is_displayed()

    def test_switch_to_fillings(self, driver):
        # Переключаемся на вкладку "Начинки"
        fillings_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, FILLINGS_SECTION)))
        fillings_element.click()
        # Проверяем, что ранее скрытый элемент стал видимым
        element_filling = driver.find_element(By.XPATH, SOME_FILLING)
        assert element_filling.is_displayed()
