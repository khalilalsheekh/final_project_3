import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from infra.browser_wrapper.base_page import BasePage


class LoginPage(BasePage):
    EMAIL_INPUT = '//input[@id="element-0"]'
    PASSWORD_INPUT = '//input[@id="element-3"]'
    LOGIN_SUBMIT_BUTTON = '//button[@data-gtm-id="start-email-login"]'
    ERROR_MESSAGE = '//div[text()="Please enter a valid email address."]'

    def __init__(self, driver):
        super().__init__(driver)
        self._email_input = self._driver.find_element(By.XPATH, self.EMAIL_INPUT)
        self._password_input = self._driver.find_element(By.XPATH, self.PASSWORD_INPUT)
        self._login_submit_button = self._driver.find_element(By.XPATH, self.LOGIN_SUBMIT_BUTTON)

    def fill_email_input(self, email):
        self._email_input.send_keys(email)

    def fill_password_input(self, password):
        self._password_input.send_keys(password)

    def click_on_login_submit_button(self):
        self._login_submit_button.click()

    def login_process_flow(self, email, password):
        self.fill_email_input(email)
        self.fill_password_input(password)
        self.click_on_login_submit_button()
        time.sleep(10)

    def error_message_is_displayed(self):
        self._error_message = WebDriverWait(self._driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, self.ERROR_MESSAGE)))
        if self._error_message.is_displayed():
            # print("Wrong email or password.")
            return True
        # print("test failed , it should show - Wrong email or password.- .")
