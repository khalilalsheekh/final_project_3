import unittest

from todoist_api_python.api import TodoistAPI

from infra.browser.utiles import generate_random_string


class TestCreateNewTask(unittest.TestCase):
    task_id = None

    def setUp(self):
        self.api = TodoistAPI('d0673b40304d868bdb9b080bd601f210b8f8126d')

    def tearDown(self):
        self.api.delete_task(task_id=self.task_id)

    def test_create_new_task(self):
        self.name_create_task = generate_random_string(5)

        response = self.api.add_task(content=self.name_create_task)
        self.task_id = response.id

        self.assertEqual(self.name_create_task, response.content)
        self.assertEqual(self.task_id, response.id)
