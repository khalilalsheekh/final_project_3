import unittest
from todoist_api_python.api import TodoistAPI
from infra.browser.utiles import generate_random_string


class TestDeleteProject(unittest.TestCase):

    def setUp(self):
        self.api = TodoistAPI('d0673b40304d868bdb9b080bd601f210b8f8126d')
        name_add_project = generate_random_string(5)
        response = self.api.add_project(name=name_add_project)
        self.project_id = response.id

    def tearDown(self):
        self.api.delete_project(project_id=self.project_id)

    def test_delete_project(self):
        # Arrange
        project_id = self.project_id

        # Act
        delete_response = self.api.delete_project(project_id=project_id)

        # Assert
        self.assertTrue(delete_response, True)
