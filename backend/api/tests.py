from http import HTTPStatus

from api import models
from django.test import Client, TestCase


class TaskiAPITestCase(TestCase):
    def setUp(self):
        self.guest_client = Client()

    def test_list_exists(self):
        """Check availability of tasks list."""
        response = self.guest_client.get("/api/tasks/")
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_task_creation(self):
        """Check creation task."""
        data = {"title": "Test", "description": "Test"}
        response = self.guest_client.post("/api/tasks/", data=data)
        self.assertEqual(response.status_code, HTTPStatus.CREATED)
        self.assertTrue(models.Task.objects.filter(title="Test").exists())
