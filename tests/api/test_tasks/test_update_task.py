import unittest
from todoist_api_python.api import TodoistAPI

from infra.browser.utiles import generate_random_string


class TestUpdateTask(unittest.TestCase):
    task_id = None

    def setUp(self):
        self.api = TodoistAPI('d0673b40304d868bdb9b080bd601f210b8f8126d')
        name_add_task = generate_random_string(5)
        response = self.api.add_task(content=name_add_task)
        self.task_id = response.id

    def tearDown(self):
        self.api.delete_task(task_id=self.task_id)

    def test_update_new_project(self):
        name_update_task = generate_random_string(5)

        response = self.api.update_task(task_id=self.task_id, content=name_update_task)

        self.assertEqual(response['content'], name_update_task)
        self.assertEqual(response["id"], self.task_id)
