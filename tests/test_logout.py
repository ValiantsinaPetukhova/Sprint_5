from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import *


class TestLogout:
    def test_logout(self, new_user_registration, driver_creation):
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
        # Нажимаем кнопку Выход
        driver.find_element(By.XPATH, LOGOUT_BUTTON).click()
        WebDriverWait(driver, 4).until(
            expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, LOGIN_PAGE)))
        login_page = driver.find_element(By.CSS_SELECTOR, LOGIN_PAGE)
        # Проверяем, что отображается страница входа
        assert login_page.is_displayed()
        driver.quit()


