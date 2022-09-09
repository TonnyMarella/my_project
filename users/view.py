from rest_framework.response import Response
from rest_framework.decorators import api_view

from users.serializers import RegistrationSerializer


@api_view(['POST', 'GET'])
def registration_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(request.data)
        return Response(serializer.errors)
