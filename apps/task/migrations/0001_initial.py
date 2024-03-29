# Generated by Django 4.1.6 on 2023-02-09 00:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Task",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(max_length=50, verbose_name="title"),
                ),
                ("description", models.TextField(verbose_name="description")),
                (
                    "creation_date",
                    models.DateTimeField(
                        default=django.utils.timezone.now,
                        verbose_name="creation date",
                    ),
                ),
                (
                    "deleted",
                    models.BooleanField(default=False, verbose_name="deleted"),
                ),
                (
                    "state",
                    models.IntegerField(
                        choices=[(0, "UNCOMPLETED"), (1, "COMPLETED")],
                        default=0,
                        verbose_name="state",
                    ),
                ),
                (
                    "priority",
                    models.IntegerField(
                        choices=[(0, "LOW"), (1, "MEDIUM"), (2, "HIGH")],
                        default=0,
                        verbose_name="priority",
                    ),
                ),
                (
                    "tag",
                    models.CharField(
                        choices=[
                            ("JB", "JOB"),
                            ("UN", "UNIVERSITY"),
                            ("HM", "HOME"),
                            ("FR", "FRIENDS"),
                            ("NT", "NOT TAG"),
                        ],
                        default="NT",
                        max_length=5,
                        verbose_name="tag",
                    ),
                ),
                (
                    "ending_date",
                    models.DateTimeField(
                        null=True, verbose_name="ending date"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="tasks",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
