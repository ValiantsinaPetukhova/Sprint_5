from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import *


class TestRegistration:
    def test_successful_registration(self, generate_email, generate_password, driver_creation):
        driver = driver_creation
        name = "Valentina"
        email = generate_email
        password = generate_password
        driver.find_element(By.XPATH, LOGIN_ACCOUNT_BUTTON).click()
        driver.find_element(By.LINK_TEXT, REGISTER_LINK).click()
        driver.find_element(By.XPATH, NAME_REGISTRATION_INPUT).send_keys(name)
        driver.find_element(By.XPATH, EMAIL_REGISTRATION_INPUT).send_keys(email)
        driver.find_element(By.XPATH, PASSWORD_REGISTRATION_INPUT).send_keys(password)
        driver.find_element(By.XPATH, REGISTER_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, LOGIN_PAGE)))

        # Проверяем успешную регистрацию, пробуем ввести логин и пароль
        driver.find_element(By.CSS_SELECTOR, LOGIN_INPUT).send_keys(email)
        driver.find_element(By.CSS_SELECTOR, PASSWORD_INPUT).send_keys(password)
        # Проверяем, что после успешного входа произошел переход на главную страницу
        assert driver.find_element(By.CLASS_NAME, MAIN_PAGE).is_displayed()
        driver.quit()

    def test_registration_with_invalid_password(self, generate_email, driver_creation):
        # Данные для регистрации
        driver = driver_creation
        email = generate_email
        name = "Valentina"
        invalid_password = "short"

        # Переход на страницу регистрации ввод данных
        driver.find_element(By.XPATH, LOGIN_ACCOUNT_BUTTON).click()
        driver.find_element(By.LINK_TEXT, REGISTER_LINK).click()
        driver.find_element(By.XPATH, NAME_REGISTRATION_INPUT).send_keys(name)
        driver.find_element(By.XPATH, EMAIL_REGISTRATION_INPUT).send_keys(email)
        driver.find_element(By.XPATH, PASSWORD_REGISTRATION_INPUT).send_keys(invalid_password)
        driver.find_element(By.XPATH, REGISTER_BUTTON).click()

        # Проверяем наличие сообщения об ошибке
        error_message = driver.find_element(By.CSS_SELECTOR, ERROR_MESSAGE_PASSWORD)
        assert error_message.is_displayed()
        driver.quit()


