import time
import unittest
from infra.browser_wrapper.logging_basicConfig import LoggingSetup

from infra.browser_wrapper.browser_wrapper import BrowserWrapper
from infra.browser_wrapper.config_provider import ConfigProvider
from logic.browser.home_page import HomePage
from logic.browser.login_page import LoginPage


class TestLogin(unittest.TestCase):
    config = ConfigProvider.load_config_json('../../config.json')

    def setUp(self):
        self.browser = BrowserWrapper()
        self.driver = self.browser.get_driver(self.config["Url"])
        # time.sleep(7)

    def test_successfully_login(self):  #login with a valid email and password
        self.login = LoginPage(self.driver)
        self.login.login_process_flow(self.config["Email"], self.config["Password"])
        self.home_page = HomePage(self.driver)
        self.assertEqual(self.driver.current_url, self.config["home-page"])

    def test_unsuccessfully_login(self):  #login wite a vaild email and an invaild
        self.login = LoginPage(self.driver)
        self.login.login_process_flow(self.config["wrong_email"], self.config["Password"])
        self.assertTrue(self.login.error_message_is_displayed())

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
