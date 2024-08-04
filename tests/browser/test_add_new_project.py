import unittest

import logging

from infra.browser_wrapper.browser_wrapper import BrowserWrapper
from infra.browser_wrapper.config_provider import ConfigProvider
from infra.browser_wrapper.logging_basicConfig import LoggingSetup
from logic.browser.home_page import HomePage
from logic.browser.login_page import LoginPage


class AddNewProject(unittest.TestCase):
    config = ConfigProvider.load_config_json('../../config.json')

    def setUp(self):
        self.browser = BrowserWrapper()
        self.driver = self.browser.get_driver(self.config["home-page"])
        login = LoginPage(self.driver)
        login.login_process_flow(self.config["Email"], self.config["Password"])

    def tearDown(self):
        self.driver.close()

    def test_add_new_project_process(self):
        """
        Test the process of adding a new project.

        This test verifies that a user can successfully create a new project
        and that the project appears in My projects after creation.
        """
        logging.info("Starting test_add_new_project_process")

        # Arrange
        self.new_project = HomePage(self.driver)

        # Act
        self.new_project.create_an_new_project_process(self.config["new_name_project"])

        # Assert
        self.assertTrue(self.new_project.project_name_is_displayed(self.config["new_name_project"]))

        logging.info("Completed test_add_new_project_process")


if __name__ == '__main__':
    LoggingSetup.setup_logging()
    unittest.main()
