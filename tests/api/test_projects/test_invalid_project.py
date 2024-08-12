import unittest
from todoist_api_python.api import TodoistAPI
from todoist_api_python.models import Project

from infra.config_provider import ConfigProvider


class TestTodoistAPI(unittest.TestCase):
    config = ConfigProvider.load_config_json('C:\\Users\\User\\PycharmProjects\\project3\\config.json')

    def setUp(self):
        self.api = TodoistAPI("d0673b40304d868bdb9b080bd601f210b8f8126d")

        for i in range(5):
            self.api.add_project(name=f"Test Project {i + 1}")

    def tearDown(self):
        projects = self.api.get_projects()
        for project in projects:
            self.api.delete_project(project.id)

    def test_add_sixth_project(self):
        # Try adding a 6th project
        response = self.api.add_project(name=self.config["six_project"])

        # Check if the response is None, which might indicate a failure
        self.assertIsNone(response.name, self.config["six_project"])
