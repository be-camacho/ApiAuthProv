from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import UserSerializer as US

class UserViewSet(viewsets.ModelViewSet):
    @action(detail=False, methods=['post'], url_path='auth')
    def auth(self, request):
        serializer = US(data=request.data)

        if serializer.is_valid():
            return Response(serializer.validated_data, status=200)
        
        return Response(serializer.errors, status=400)
# Create your views here.
