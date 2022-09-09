from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework import viewsets
from rest_framework import mixins

from .models import Task
from .serializers import TaskAdminSerializer, TaskUserSerializer


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskAdminSerializer
    queryset = Task.objects.all()
    permission_classes = (IsAdminUser,)


class TaskUserViewSet(viewsets.ReadOnlyModelViewSet, mixins.UpdateModelMixin):
    serializer_class = TaskUserSerializer
    queryset = Task.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return self.queryset.filter(executor=self.request.user.id)
