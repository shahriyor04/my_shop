from rest_framework.serializers import ModelSerializer
from .models import User

class UserProfileSerializers(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']

