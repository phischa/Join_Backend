from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.shortcuts import get_object_or_404
from join_app.models import User, Task, Contact

from .serializers import UserSerializer

from rest_framework import mixins, generics, viewsets

@api_view(['GET'])
def first_view(request):
    return Response({"message":"Hallo World!"})

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer