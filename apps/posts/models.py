from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone


# Saving media locally is not a good practice 
# for a big social network actually. GoogleCloud or AWS 
# migth be a better alternative
def get_user_image_path(instance, filename):
    return f'users/{instance.author}/posts/{instance.id}/{filename}'


class Post(models.Model):
    author = models.ForeignKey(
        to=get_user_model(),
        null=True,
        on_delete=models.SET_NULL,
        related_name='posts'
    )
    image = models.ImageField(
        upload_to=get_user_image_path,
        blank=True,
        null=True,
    )
    text = models.CharField(
        max_length=8192,
        blank=True
    )
    likes = models.ManyToManyField(
        to=get_user_model(),
        blank=True,
        through='Like'
    )
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def count_likes(self):
        return len(self.likes.all())


class Like(models.Model):
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE
    )
    date = models.DateTimeField(default=timezone.now)
