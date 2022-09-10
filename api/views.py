from rest_framework.permissions import IsAdminUser
from rest_framework import viewsets
from rest_framework import mixins
from api.models import Task
from api.serializers import TaskAdminSerializer, TaskUserSerializer


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskAdminSerializer
    queryset = Task.objects.all()
    permission_classes = (IsAdminUser,)


class TaskUserViewSet(viewsets.ReadOnlyModelViewSet, mixins.UpdateModelMixin):
    serializer_class = TaskUserSerializer
    queryset = Task.objects.all()

    def get_queryset(self):
        return self.queryset.filter(executor=self.request.user.id)
