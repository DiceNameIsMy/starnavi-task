from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED ,HTTP_204_NO_CONTENT
from rest_framework.filters import OrderingFilter

from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError
from django.utils.timezone import datetime, make_aware

from django_filters.rest_framework import DjangoFilterBackend

from .serializers import PostSerializer
from .services import get_likes_stats
from ...permissons import IsAuthor
from ...models import Post, Like
from ...filters import DateFilter


class ListCreatePostView(ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly, )

    filter_backends = [DjangoFilterBackend, OrderingFilter, DateFilter]
    filterset_fields = ['author']
    ordering = ['created_at', 'updated_at' ]
    date_fields = ['created_at', 'updated_at']

    queryset = Post.objects.all()
    serializer_class = PostSerializer


class RetrieveUpdateDestroyPostView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly, )

    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostStatsView(GenericAPIView):
    permission_classes = (IsAuthenticated, IsAuthor)

    queryset = Post.objects.all()

    def get(self, request, pk):
        start_date = request.GET.get('start_date')
        end_date = request.GET.get('end_date', str(datetime.today().date()))

        if not start_date:
            raise ValidationError("start_date should be provided")

        # TODO better naming
        start_date_date = make_aware(datetime.strptime(start_date, "%Y-%m-%d"))
        end_date_date = make_aware(datetime.strptime(end_date, "%Y-%m-%d"))

        post: Post = self.get_object()

        stats = get_likes_stats(post, start_date_date, end_date_date)

        return Response(stats)


class LikePostView(APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request, pk):
        post: Post = get_object_or_404(Post, pk=pk)
        post.likes.add(request.user)

        return Response(status=HTTP_201_CREATED)

    def delete(self, request, pk):
        post: Post = get_object_or_404(Post, pk=pk)
        post.likes.remove(request.user)

        return Response(status=HTTP_204_NO_CONTENT)
