from rest_framework.serializers import ModelSerializer
from django.core.exceptions import ValidationError

from ...models import Post, Like


class PostSerializer(ModelSerializer):

    def validate(self, attrs):
        if not any([attrs.get('image'), attrs.get('text')]):
            raise ValidationError("test")
        return attrs

    class Meta:
        model = Post
        fields = (
            'author', 
            'image', 'text', 'count_likes', 
            'created_at', 'updated_at'
        )
        optional_fields = (
            'image', 'text','count_likes', 
            'created_at', 'updated_at', 
        )
        validators = []
