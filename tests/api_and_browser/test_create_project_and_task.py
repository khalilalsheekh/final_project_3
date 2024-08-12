import unittest

from todoist_api_python.api import TodoistAPI

from infra.browser.browser_wrapper import BrowserWrapper
from infra.browser.utiles import generate_random_string
from infra.config_provider import ConfigProvider
from logic.browser.home_page import HomePage
from logic.browser.login_page import LoginPage


class TestCreateProjectAndTask(unittest.TestCase):
    config = ConfigProvider.load_config_json('C:\\Users\\User\\PycharmProjects\\project3\\config.json')

    def setUp(self):
        """Set up the API, create a project and task, and log in to the website."""
        self.task_name = generate_random_string(8)
        self.due_date = self.config["due_string"]
        self.api = TodoistAPI(self.config["token"])
        self.add_project = self.api.add_project(name=self.config["add_project"])
        self.add_task = self.api.add_task(content=self.task_name, project_id=self.add_project.id,
                                          Priority=4,
                                          due_string=self.due_date)
        self.browser = BrowserWrapper()
        self.driver = self.browser.get_driver(self.config["home-page"])
        login = LoginPage(self.driver)
        login.login_process_flow(self.config["Email"], self.config["Password"])

    def tearDown(self):
        self.api.delete_project(project_id=self.add_project.id)

    def test_create_project_and_task(self):
        """Check that the task name, due date, and priority are displayed in the UI."""
        # Arrange
        press_on_project_and_task = HomePage(self.driver)

        # Act
        press_on_project_and_task.create_project_and_task_flow()

        # Assert
        self.assertTrue(press_on_project_and_task.new_project_name_is_displayed())
        self.assertTrue(press_on_project_and_task.task_name_is_displayed(self.task_name))
        self.assertTrue(press_on_project_and_task.priority_is_displayed())
        self.assertEqual(press_on_project_and_task.get_final_task_due_date(), self.due_date)
