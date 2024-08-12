import unittest
from todoist_api_python.api import TodoistAPI

from infra.browser.utiles import generate_random_string


class TestCloseTask(unittest.TestCase):
    def setUp(self):
        self.api = TodoistAPI('d0673b40304d868bdb9b080bd601f210b8f8126d')
        name_add_task = generate_random_string(5)
        response = self.api.add_task(content=name_add_task)
        self.task_id = response.id

    def tearDown(self):
        self.api.delete_task(task_id=self.task_id)

    def test_close_task(self):
        task_id = self.task_id

        close_task_response = self.api.close_task(task_id=task_id)

        self.assertEqual(close_task_response, True)
