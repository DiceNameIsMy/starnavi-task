from rest_framework.generics import RetrieveAPIView
from django.contrib.auth import get_user_model

from .serializers import UserProfileSerializer


UserModel = get_user_model()

class RetrieveUserView(RetrieveAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserProfileSerializer