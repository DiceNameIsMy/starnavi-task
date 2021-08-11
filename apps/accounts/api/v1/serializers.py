from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model


UserModel = get_user_model()


class UserDetailsSerializer(ModelSerializer):
    class Meta:
        model = UserModel
        fields = (
            'pk', 'username', 'email', 
            'first_name', 'last_name', 
            'last_login', 'last_active'
        )

