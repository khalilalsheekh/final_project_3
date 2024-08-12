import unittest
from todoist_api_python.api import TodoistAPI
from infra.browser.utiles import generate_random_string


class TestDeleteComment(unittest.TestCase):
    def setUp(self):
        self.api = TodoistAPI('d0673b40304d868bdb9b080bd601f210b8f8126d')
        name_new_task_comment = generate_random_string(6)
        self.response_new_task = self.api.add_task(content=name_new_task_comment)
        name_add_new_comment = generate_random_string(5)
        self.response_new_comment = self.api.add_comment(content=name_add_new_comment,task_id=self.response_new_task.id)

    def tearDown(self):
        self.api.delete_task(task_id=self.response_new_task.id)

    def test_delete_comment(self):
        delete_response = self.api.delete_comment(comment_id=self.response_new_comment.id)
        self.assertTrue(delete_response, "")

