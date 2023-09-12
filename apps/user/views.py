from .serializers import UserProfileSerializers
# from .permission import UserPermission
from rest_framework.viewsets import ModelViewSet
from .models import User


class UserProfileViewSet(ModelViewSet):
    serializer_class = UserProfileSerializers
    queryset = User.objects.all()
    # permission_classes = (UserPermission, )
