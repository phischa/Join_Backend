from rest_framework import serializers
from rest_framework import status

from join_app.models import User, Task, Contact

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = []