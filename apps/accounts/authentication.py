from rest_framework_simplejwt.authentication import JWTAuthentication

from django.utils import timezone


class CustomJWTAuthentication(JWTAuthentication):

    @staticmethod
    def update_user_last_login(user):
        print(user)
        user.last_active = timezone.now()
        user.save()

    def get_user(self, validated_token):
        user = super().get_user(validated_token)
        self.update_user_last_login(user)
        return user
