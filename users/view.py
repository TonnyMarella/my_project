from rest_framework.response import Response
from rest_framework.decorators import api_view

from users.serializers import RegistrationSerializer


@api_view(['POST'])
def registration_view(request):
    serializer = RegistrationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(request.data)
    return Response(serializer.errors)
