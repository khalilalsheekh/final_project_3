import unittest

import logging

from infra.browser_wrapper.browser_wrapper import BrowserWrapper
from infra.browser_wrapper.config_provider import ConfigProvider
from infra.browser_wrapper.logging_basicConfig import LoggingSetup
from infra.browser_wrapper.utiles import generate_random_string
from logic.browser.home_page import HomePage
from logic.browser.inbox_page import InboxPage
from logic.browser.login_page import LoginPage


class TestCreateComment(unittest.TestCase):
    config = ConfigProvider.load_config_json('../../config.json')

    def setUp(self):
        self.browser = BrowserWrapper()
        self.driver = self.browser.get_driver(self.config["home-page"])
        login = LoginPage(self.driver)
        login.login_process_flow(self.config["Email"], self.config["Password"])

    def test_create_new_comment_process(self):
        """
        Test the process of creating a new comment.

        This test verifies that a user can successfully create a new comment
        and that the comment is displayed after creation.
        """
        logging.info("Starting test_create_new_comment_process")

        # Arrange
        new_comment = generate_random_string(6)
        self.comments_button = HomePage(self.driver)
        self.comment_process = InboxPage(self.driver)

        # Act
        self.comments_button.click_on_inbox_button()
        self.comment_process.create_a_new_comment_process_flow(new_comment)

        # Assert
        self.assertTrue(self.comment_process.comment_is_displayed(new_comment))

        logging.info("Completed test_create_new_comment_process")


if __name__ == '__main__':
    LoggingSetup.setup_logging()
    unittest.main()
