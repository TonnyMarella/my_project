from rest_framework import serializers

from .models import Task


class TaskAdminSerializer(serializers.ModelSerializer):
    # author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Task
        fields = ['author', 'title', 'exercise', 'executor', 'status']


class TaskUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['author', 'title', 'exercise', 'executor', 'status']
        read_only_fields = ('title', 'author', 'exercise', 'executor')
