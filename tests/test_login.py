from selenium.webdriver.common.by import By
from locators import *


class TestLogin:
    def test_login_using_button_on_the_main_page(self, new_user_registration, driver):
        email = new_user_registration[0]
        password = new_user_registration[1]
        # Нажимаем на кнопку Войти в аккаунт и вводим данные
        driver.find_element(By.XPATH, LOGIN_ACCOUNT_BUTTON).click()
        driver.find_element(By.CSS_SELECTOR, LOGIN_INPUT).send_keys(email)
        driver.find_element(By.CSS_SELECTOR, PASSWORD_INPUT).send_keys(password)
        driver.find_element(By.XPATH, LOGIN_BUTTON).click()
        # Проверяем, что после успешного входа произошел переход на главную страницу
        assert driver.find_element(By.CLASS_NAME, MAIN_PAGE).is_displayed()

    def test_login_using_personal_cabinet_button(self, driver, new_user_registration):
        email = new_user_registration[0]
        password = new_user_registration[1]
        # Нажимаем на кнопку Личный кабинет и вводим данные
        driver.find_element(By.XPATH, PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(By.CSS_SELECTOR, LOGIN_INPUT).send_keys(email)
        driver.find_element(By.CSS_SELECTOR, PASSWORD_INPUT).send_keys(password)
        driver.find_element(By.XPATH, LOGIN_BUTTON).click()
        # Проверяем, что после успешного входа произошел переход на главную страницу
        assert driver.find_element(By.CLASS_NAME, MAIN_PAGE).is_displayed()

    def test_login_through_button_in_registration_form(self, driver, new_user_registration):
        email = new_user_registration[0]
        password = new_user_registration[1]
        # Переходим в форму регистрации, нажимаем кнопку Войти и вводим данные
        driver.find_element(By.XPATH, LOGIN_ACCOUNT_BUTTON).click()
        driver.find_element(By.LINK_TEXT, REGISTER_LINK).click()
        driver.find_element(By.LINK_TEXT, LOGIN_LINK).click()
        driver.find_element(By.CSS_SELECTOR, LOGIN_INPUT).send_keys(email)
        driver.find_element(By.CSS_SELECTOR, PASSWORD_INPUT).send_keys(password)
        driver.find_element(By.XPATH, LOGIN_BUTTON).click()
        # Проверяем, что после успешного входа произошел переход на главную страницу
        assert driver.find_element(By.CLASS_NAME, MAIN_PAGE).is_displayed()

    def test_login_through_button_recovery_button(self, driver, new_user_registration):
        email = new_user_registration[0]
        password = new_user_registration[1]
        # Переходим в форму авторизации, нажимаем кнопку восстановить пароль и вводим данные
        driver.find_element(By.XPATH, LOGIN_ACCOUNT_BUTTON).click()
        driver.find_element(By.LINK_TEXT, RECOVER_PASSWORD).click()
        driver.find_element(By.LINK_TEXT, LOGIN_LINK).click()
        driver.find_element(By.CSS_SELECTOR, LOGIN_INPUT).send_keys(email)
        driver.find_element(By.CSS_SELECTOR, PASSWORD_INPUT).send_keys(password)
        driver.find_element(By.XPATH, LOGIN_BUTTON).click()
        # Проверяем, что после успешного входа произошел переход на главную страницу
        assert driver.find_element(By.CLASS_NAME, MAIN_PAGE).is_displayed()


if __name__ == "__main__":
    pass

