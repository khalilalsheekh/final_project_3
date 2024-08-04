import unittest

import logging

from infra.browser_wrapper.browser_wrapper import BrowserWrapper
from infra.browser_wrapper.config_provider import ConfigProvider
from infra.browser_wrapper.logging_basicConfig import LoggingSetup
from logic.browser.home_page import HomePage
from logic.browser.login_page import LoginPage


class TestSearch(unittest.TestCase):
    config = ConfigProvider.load_config_json('../../config.json')

    def setUp(self):
        self.browser = BrowserWrapper()
        self.driver = self.browser.get_driver(self.config["home-page"])
        login = LoginPage(self.driver)
        login.login_process_flow(self.config["Email"], self.config["Password"])

    def test_search_successfully(self):
        """
        Test the search functionality with valid input.

        This test verifies that when a user performs a search with valid text,
        they are redirected to the correct page.
        """
        logging.info("Starting test_search_successfully")

        # Arrange
        search_button = HomePage(self.driver)

        # Act
        search_button.search_button_with_input_flow(self.config["valid_text"])

        # Assert
        self.assertEqual(self.driver.current_url, self.config["upcoming_page"])

        logging.info("Completed test_search_successfully")

    def test_search_unsuccessfully(self):
        """
        Test the search functionality with invalid input.

        This test verifies that when a user performs a search with invalid text,
        a "no results" message is displayed.
        """
        logging.info("Starting test_search_unsuccessfully")

        # Arrange
        search_button = HomePage(self.driver)
        search_input = HomePage(self.driver)

        # Act
        search_button.click_on_search_button()
        search_input.search_process_unsuccessfully_flow(self.config["invalid_text"])

        # Assert
        self.assertTrue(search_input.no_results_text_is_displayed())

        logging.info("Completed test_search_unsuccessfully")

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    LoggingSetup.setup_logging()
    unittest.main()
