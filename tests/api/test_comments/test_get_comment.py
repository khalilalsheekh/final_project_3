import unittest
from todoist_api_python.api import TodoistAPI
from infra.browser.utiles import generate_random_string


class TestGetComment(unittest.TestCase):
    def setUp(self):
        self.api = TodoistAPI('d0673b40304d868bdb9b080bd601f210b8f8126d')
        self.task_name = generate_random_string(5)
        self.task = self.api.add_task(content=self.task_name)  # Create a new task
        self.comment_name = generate_random_string(5)
        self.response_add_comment = self.api.add_comment(content=self.comment_name, task_id=self.task.id)

    def tearDown(self):
        self.api.delete_comment(comment_id=self.response_add_comment.id)
        self.api.delete_task(task_id=self.task.id)

    def test_get_comment(self):
        self.api = TodoistAPI('d0673b40304d868bdb9b080bd601f210b8f8126d')

        response = self.api.get_comment(comment_id=self.response_add_comment.id)

        self.assertEqual(response.id, self.response_add_comment.id)
        self.assertEqual(response.content, self.comment_name)
