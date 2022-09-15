from rest_framework import serializers
from api.models import Task
from api.tasks import send_mail_task


class TaskAdminSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        mail_to = validated_data['executor'].email
        send_mail_task.delay(mail_to)
        return Task.objects.create(**validated_data)

    class Meta:
        model = Task
        fields = ['author', 'title', 'exercise', 'executor', 'status', 'created_at', 'modified_at']


class TaskUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ['author', 'title', 'exercise', 'executor', 'status', 'created_at', 'modified_at']
        read_only_fields = ('title', 'author', 'exercise', 'executor', 'created_at', 'modified_at')
