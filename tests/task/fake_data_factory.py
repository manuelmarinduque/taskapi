from random import choice

from faker import Faker

from apps.task.models import Task


faker = Faker()


class TaskFactory:
    @staticmethod
    def get_task_fake_data(user=1):
        return {
            "title": faker.text(50),
            "description": faker.text(100),
            "priority": faker.random_int(0, 2),
            "tag": choice(["JB", "UN", "HM", "FR", "NT"]),
            "ending_date": faker.date_this_year(),
            "user": user,
        }

    @staticmethod
    def create_task(user):
        return Task.objects.create(**TaskFactory.get_task_fake_data(user))
