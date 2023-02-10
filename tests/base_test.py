from faker import Faker
from rest_framework import status
from rest_framework.test import APITestCase

from apps.user.models import User


class BaseTest(APITestCase):
    def setUp(self):
        faker = Faker()
        self.login_url = "/user/login"
        self.user = User.objects.create_superuser(
            first_name="Tests",
            last_name="Cases",
            username=faker.name(),
            password="development",
            email=faker.email(),
        )
        response = self.client.post(
            self.login_url,
            {"username": self.user.username, "password": "development"},
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.token = response.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.token}")
        return super().setUp()
