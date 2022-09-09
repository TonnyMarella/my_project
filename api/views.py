from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework import viewsets, status
from rest_framework import mixins
from django.core.mail import send_mail
from rest_framework.response import Response
from django.urls import reverse_lazy

from MAIN_APP import settings
from api.models import Task
from api.serializers import TaskAdminSerializer, TaskUserSerializer
from api.forms import RegisterUserForm


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


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'api/registration.html'

    def get_success_url(self):
        return reverse_lazy('login')


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'api/login.html'
