from rest_framework import serializers
from api.models import Task


class TaskAdminSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ['author', 'title', 'exercise', 'executor', 'status', 'created_at', 'modified_at']


class TaskUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ['author', 'title', 'exercise', 'executor', 'status', 'created_at', 'modified_at']
        read_only_fields = ('title', 'author', 'exercise', 'executor', 'created_at', 'modified_at')
