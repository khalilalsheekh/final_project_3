import unittest

from todoist_api_python.api import TodoistAPI

from infra.browser.utiles import generate_random_string


class TestCreateNewTask(unittest.TestCase):
    task_id = None

    def setUp(self):
        self.api = TodoistAPI('d0673b40304d868bdb9b080bd601f210b8f8126d')
        self.content_name = generate_random_string(5)
        # Create a task and store its ID
        response = self.api.add_task(content=self.content_name)
        self.task_id = response.id

    def tearDown(self):
        self.api.delete_task(task_id=self.task_id)

    def test_get_an_active_task(self):
        task_id = self.task_id

        response = self.api.get_task(task_id=task_id)

        self.assertEqual(task_id, response.id)
        self.assertEqual(self.content_name, response.content)
