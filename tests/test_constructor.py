from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *


class TestConstructor:
    def test_switch_to_buns(self, driver):
        # Переключаемся на вкладку "Соусы", а затем возвращаемся на "Булки"
        sauces_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, SAUCES_SECTION)))
        sauces_element.click()
        class_before = driver.find_element(By.XPATH, BUNS_SECTION).get_attribute('class')
        # Проверяем, что класс не содержит tab_tab_type_current__2BEPc
        assert 'tab_tab_type_current__2BEPc' not in class_before

        buns_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, BUNS_SECTION)))
        buns_element.click()

        # Проверяем, что класс изменился
        class_after = driver.find_element(By.XPATH, BUNS_SECTION).get_attribute('class')
        assert 'tab_tab_type_current__2BEPc' in class_after

    def test_switch_to_sauces(self, driver):
        # Проверяем, что класс не содержит tab_tab_type_current__2BEPc
        class_before = driver.find_element(By.XPATH, SAUCES_SECTION).get_attribute('class')
        assert 'tab_tab_type_current__2BEPc' not in class_before
        # Переключаемся на вкладку "Соусы"
        sauces_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, SAUCES_SECTION)))
        sauces_element.click()
        # Проверяем, что класс изменился
        class_after = driver.find_element(By.XPATH, SAUCES_SECTION).get_attribute('class')
        assert 'tab_tab_type_current__2BEPc' in class_after

    def test_switch_to_fillings(self, driver):
        # Проверяем, что класс не содержит tab_tab_type_current__2BEPc
        class_before = driver.find_element(By.XPATH, FILLINGS_SECTION).get_attribute('class')
        assert 'tab_tab_type_current__2BEPc' not in class_before
        # Переключаемся на вкладку "Начинки"
        fillings_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, FILLINGS_SECTION)))
        fillings_element.click()
        # Проверяем, что класс изменился
        class_after = driver.find_element(By.XPATH, FILLINGS_SECTION).get_attribute('class')
        assert 'tab_tab_type_current__2BEPc' in class_after
