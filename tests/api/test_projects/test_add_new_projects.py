import unittest
from todoist_api_python.api import TodoistAPI
from infra.browser.utiles import generate_random_string


class TestAddNewProject(unittest.TestCase):
    project_id = None

    def setUp(self):
        self.api = TodoistAPI('d0673b40304d868bdb9b080bd601f210b8f8126d')
        name_add_project = generate_random_string(5)
        response = self.api.add_project(name=name_add_project)
        self.project_id = response.id

    def tearDown(self):
        self.api.delete_project(project_id=self.project_id)

    def test_add_new_project(self):
        response = self.api.get_project(project_id=self.project_id)

        # Verify that the project was created successfully
        self.assertIsNotNone(response)
        self.assertEqual(response.id, self.project_id)

    # def test_update_a_project(self):
    #     name_update_project = generate_random_string(5)
    #
    #     response = self.api.update_project(project_id=CreateANewProject.project_id, name=name_update_project)
    #
    #     self.assertEqual(response['name'], name_update_project)


if __name__ == '__main__':
    unittest.main()
