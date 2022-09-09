from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework import viewsets, status
from rest_framework import mixins
from django.core.mail import send_mail
from rest_framework.response import Response

from MAIN_APP import settings
from api.models import Task
from api.serializers import TaskAdminSerializer, TaskUserSerializer


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskAdminSerializer
    queryset = Task.objects.all()
    permission_classes = (IsAdminUser,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        send_mail('Your New Task', 'Write program Hello World', settings.EMAIL_HOST_USER, ['temazubkov02@gmail.com'])
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class TaskUserViewSet(viewsets.ReadOnlyModelViewSet, mixins.UpdateModelMixin):
    serializer_class = TaskUserSerializer
    queryset = Task.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return self.queryset.filter(executor=self.request.user.id)
