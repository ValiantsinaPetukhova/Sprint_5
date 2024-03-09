from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import *


class TestSwitchFromAccount:

    def test_switch_from_personal_account_to_constructor(self, new_user_registration, driver_creation):
        driver = driver_creation
        email = new_user_registration[0]
        password = new_user_registration[1]
        # Login
        driver.find_element(By.XPATH, LOGIN_ACCOUNT_BUTTON).click()
        driver.find_element(By.CSS_SELECTOR, LOGIN_INPUT).send_keys(email)
        driver.find_element(By.CSS_SELECTOR, PASSWORD_INPUT).send_keys(password)
        driver.find_element(By.XPATH, LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.CLASS_NAME, MAIN_PAGE)))
        # Переходим в личный кабинет
        driver.find_element(By.XPATH, PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 4).until(
            expected_conditions.visibility_of_element_located((By.LINK_TEXT, PROFILE_PAGE)))
        # Переходим к конструктор
        driver.find_element(By.XPATH, CONSTRUCTOR_BUTTON).click()
        constructor_page = driver.find_element(By.CLASS_NAME, CONSTRUCTOR_PAGE)
        # Проверяем, что отображается страница с конструктором
        assert constructor_page.is_displayed()
        driver.quit()

    def test_click_from_personal_to_logo(self, new_user_registration, driver_creation):
        driver = driver_creation
        email = new_user_registration[0]
        password = new_user_registration[1]
        # Login
        driver.find_element(By.XPATH, LOGIN_ACCOUNT_BUTTON).click()
        driver.find_element(By.CSS_SELECTOR, LOGIN_INPUT).send_keys(email)
        driver.find_element(By.CSS_SELECTOR, PASSWORD_INPUT).send_keys(password)
        driver.find_element(By.XPATH, LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.CLASS_NAME, MAIN_PAGE)))
        # Переходим в личный кабинет
        driver.find_element(By.XPATH, PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 4).until(
            expected_conditions.visibility_of_element_located((By.LINK_TEXT, PROFILE_PAGE)))
        # Нажимаем на логотип
        driver.find_element(By.CSS_SELECTOR, LOGO_AREA).click()
        main_page = driver.find_element(By.CLASS_NAME, MAIN_PAGE)
        # Проверяем, что отображается главная страница
        assert main_page.is_displayed()
        driver.quit()


