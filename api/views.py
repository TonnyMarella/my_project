from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from django.core.mail import send_mail, mail_admins
from django.conf import settings

from .models import Task
from .serializers import TaskAdminSerializer, TaskUserSerializer
from django.contrib.auth.models import User


class TaskAPIList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskAdminSerializer
    permission_classes = (IsAdminUser,)

    def post(self, request, *args, **kwargs):
        admin_email = request.user.email
        executor = request.data['executor']
        print(admin_email)
        user = User.objects.get(pk=executor)
        print(executor)
        print(user.email)
        subject = "New task"
        msg = "You have a new task"
        to = user.email
        res = send_mail(subject, msg, settings.EMAIL_HOST_USER, [to], fail_silently=False)
        print(res)
        return self.create(request, *args, **kwargs)


class TaskAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskAdminSerializer
    permission_classes = (IsAdminUser,)


class TaskForUserAPIList(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskUserSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self, *args, **kwargs):
        return Task.objects.filter(executor=self.request.user.id)


class TaskForUserAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskUserSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self, *args, **kwargs):
        return Task.objects.filter(executor=self.request.user.id)
