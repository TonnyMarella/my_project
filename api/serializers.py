from rest_framework import serializers
from django.core.mail import send_mail
from api.models import Task
from MAIN_APP import settings


class TaskAdminSerializer(serializers.ModelSerializer):
    send_mail('Your New Task', 'Write program Hello World', settings.EMAIL_HOST_USER, ['temazubkov02@gmail.com'])

    class Meta:
        model = Task
        fields = ['author', 'title', 'exercise', 'executor', 'status', 'created_at', 'modified_at']


class TaskUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ['author', 'title', 'exercise', 'executor', 'status', 'created_at', 'modified_at']
        read_only_fields = ('title', 'author', 'exercise', 'executor', 'created_at', 'modified_at')
