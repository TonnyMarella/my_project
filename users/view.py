from rest_framework.generics import CreateAPIView

from users.serializers import RegistrationSerializer


class RegisterUserAPIView(CreateAPIView):
    serializer_class = RegistrationSerializer
