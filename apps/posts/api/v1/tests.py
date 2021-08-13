from django.test import TestCase
from django.contrib.auth import get_user_model
from django.utils.timezone import now, make_aware, timedelta

from apps.posts.api.v1.services import get_likes_stats
from apps.posts.models import Post, Like


UserModel = get_user_model()


class ServicesTests(TestCase):

    TODAY_DATE = now()
    ONE_DAY_TIMEDELTA = timedelta(days=1)

    def setUp(self) -> None:
        for i in range(1, 5):
            u = UserModel.objects.create_user(
                username=f'test{i}',
                password='password'
            )
            p = Post.objects.create(text=f'test_text{i}')

        u1 = UserModel.objects.create_user(
            username='test5',
            password='password'
        )
        p1 = Post.objects.first()
        l1 = Like.objects.create(
            post=p1,
            author=u1,
            date=(self.TODAY_DATE - self.ONE_DAY_TIMEDELTA)
        )

        for i in range(1, 5):
            days = self.ONE_DAY_TIMEDELTA * i
            u = UserModel.objects.get(pk=i)
            l = Like.objects.create(
                post=p1,
                author=u,
                date=self.TODAY_DATE - days
            )

    def test_get_likes_stats_lenght(self):
        post = Post.objects.get(text='test_text1')
        likes = Like.objects.filter(post=post)

        stats = get_likes_stats(likes)

        self.assertEqual(len(stats), 4)

    def test_get_likes_stats_amount(self):
        post = Post.objects.get(text='test_text1')
        likes = Like.objects.filter(post=post)

        stats = get_likes_stats(likes)
        date = str((self.TODAY_DATE - self.ONE_DAY_TIMEDELTA).date())

        self.assertEqual(stats[date], 2)


    def test_get_likes_stats_empty(self):
        post = Post.objects.get(text='test_text2')
        likes = Like.objects.filter(post=post)

        stats = get_likes_stats(likes)

        self.assertFalse(stats)


