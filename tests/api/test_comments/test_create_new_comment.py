import unittest
from todoist_api_python.api import TodoistAPI
from infra.browser.utiles import generate_random_string


class CreateNewComment(unittest.TestCase):
    def setUp(self):
        self.api = TodoistAPI('d0673b40304d868bdb9b080bd601f210b8f8126d')
        self.task_name = generate_random_string(5)
        self.task = self.api.add_task(content=self.task_name)  # Create a new task

    def tearDown(self):

        self.api.delete_comment(comment_id=self.response.id)
        self.api.delete_task(task_id=self.task.id)

    def test_create_new_comment(self):
        name_add_comment = generate_random_string(5)

        # Add a comment to the created task
        self.response = self.api.add_comment(content=name_add_comment, task_id=self.task.id)

        self.assertEqual(self.response.content, name_add_comment)


