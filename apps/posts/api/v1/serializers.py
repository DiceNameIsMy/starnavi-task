from rest_framework.serializers import ModelSerializer
from django.core.exceptions import ValidationError

from ...models import Post, Like


class PostSerializer(ModelSerializer):

    def validate(self, attrs):
        if not any([attrs.get('image'), attrs.get('text')]):
            raise ValidationError("image or text should be provided")
        return attrs

    def to_representation(self, instance):
        """ Used to add field "is_liked" that shows 
        did current user liked this post
        """
        is_liked = self.context['request'].user in instance.likes.all()
        ret = super().to_representation(instance)
        ret['is_liked'] = is_liked
        return ret

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
