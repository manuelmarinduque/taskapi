from rest_framework import serializers

from .models import User
from apps.task.serializers import TaskSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "username",
            "password",
            "first_name",
            "last_name",
            "email",
        )

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        user.save()
        return user


class UserSerializerForQueries(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True)

    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "tasks",
            "last_login",
        )
