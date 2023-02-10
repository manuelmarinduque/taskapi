from rest_framework import status

from tests.base_test import BaseTest
from .fake_data_factory import TaskFactory, Task


# Create your tests here.
class TasksTests(BaseTest):
    def test_create_task_success(self):
        response = self.client.post(
            "/task/", TaskFactory.get_task_fake_data(), format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.all().count(), 1)

    def test_task_creation_fails_by_required_fields(self):
        response = self.client.post("/task/", {}, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn(
            "required", [error[0].code for error in response.data.values()]
        )

    def test_task_creation_fails_by_invalid_value_for_tag(self):
        response = self.client.post(
            "/task/",
            {**TaskFactory.get_task_fake_data(), **{"tag": 123}},
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn(
            "invalid_choice",
            [error[0].code for error in response.data.values()],
        )

    def test_task_creation_fails_by_invalid_value_for_state(self):
        response = self.client.post(
            "/task/",
            {**TaskFactory.get_task_fake_data(), **{"state": 123}},
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn(
            "invalid_choice",
            [error[0].code for error in response.data.values()],
        )

    def test_task_creation_fails_by_invalid_value_for_priority(self):
        response = self.client.post(
            "/task/",
            {**TaskFactory.get_task_fake_data(), **{"priority": 123}},
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn(
            "invalid_choice",
            [error[0].code for error in response.data.values()],
        )

    def test_get_tasks_success(self):
        response = self.client.get("/task/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_nonexistent_task(self):
        response = self.client.get("/task/3/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_task(self):
        fake_task = TaskFactory.create_task(self.user)
        response = self.client.delete(
            f"/task/{fake_task.id}/",
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.filter(id=fake_task.id).first(), None)

    def test_mark_task_as_completed(self):
        fake_task = TaskFactory.create_task(self.user)
        completed_id = 1
        response = self.client.patch(
            f"/task/{fake_task.id}/",
            {"state": completed_id},
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            Task.objects.filter(id=fake_task.id).first().state, completed_id
        )

    def test_filter_task_by_description(self):
        fake_task = TaskFactory.create_task(self.user)
        response = self.client.get(
            f"/task/?description={fake_task.description}"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            Task.objects.filter(id=fake_task.id).first().description,
            fake_task.description,
        )

    def test_filter_task_by_title(self):
        fake_task = TaskFactory.create_task(self.user)
        response = self.client.get(f"/task/?title={fake_task.title}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            Task.objects.filter(id=fake_task.id).first().title, fake_task.title
        )

    def test_filter_task_by_tag(self):
        fake_task = TaskFactory.create_task(self.user)
        response = self.client.get(f"/task/?tag={fake_task.tag}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            Task.objects.filter(id=fake_task.id).first().tag, fake_task.tag
        )

    def test_filter_task_by_state(self):
        fake_task = TaskFactory.create_task(self.user)
        response = self.client.get(f"/task/?state={fake_task.state}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            Task.objects.filter(id=fake_task.id).first().state, fake_task.state
        )

    def test_filter_task_by_priority(self):
        fake_task = TaskFactory.create_task(self.user)
        response = self.client.get(f"/task/?priority={fake_task.priority}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            Task.objects.filter(id=fake_task.id).first().priority,
            fake_task.priority,
        )

    def test_filter_task_by_multiple_keys(self):
        fake_task = TaskFactory.create_task(self.user)
        response = self.client.get(
            f"/task/?priority={fake_task.priority}&tag={fake_task.tag}"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            Task.objects.filter(id=fake_task.id).first().priority,
            fake_task.priority,
        )
