from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class State(models.IntegerChoices):
    UNCOMPLETED = 0, _("UNCOMPLETED")
    COMPLETED = 1, _("COMPLETED")


class Priority(models.IntegerChoices):
    LOW = 0, _("LOW")
    MEDIUM = 1, _("MEDIUM")
    HIGH = 2, _("HIGH")


class Tag(models.TextChoices):
    JOB = "JB", _("JOB")
    UNIVERSITY = "UN", _("UNIVERSITY")
    HOME = "HM", _("HOME")
    SOCIAL = "FR", _("FRIENDS")
    NO_TAG = "NT", _("NOT TAG")


# Create your models here.


class AbstractTask(models.Model):
    title = models.CharField(_("title"), max_length=50)
    description = models.TextField(_("description"))
    creation_date = models.DateTimeField(
        _("creation date"), default=timezone.now
    )
    deleted = models.BooleanField(_("deleted"), default=False)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


class Task(AbstractTask):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="tasks"
    )
    state = models.IntegerField(
        _("state"),
        choices=State.choices,
        default=State.UNCOMPLETED,
    )
    priority = models.IntegerField(
        _("priority"),
        choices=Priority.choices,
        default=Priority.LOW,
    )
    tag = models.CharField(
        _("tag"),
        max_length=5,
        choices=Tag.choices,
        default=Tag.NO_TAG,
    )
    ending_date = models.DateTimeField(_("ending date"), null=True)
