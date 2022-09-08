from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from .models import Task
from .serializers import TaskAdminSerializer, TaskUserSerializer


class TaskAPIList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskAdminSerializer
    permission_classes = (IsAdminUser,)


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
