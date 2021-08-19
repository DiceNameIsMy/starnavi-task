from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED ,HTTP_204_NO_CONTENT
from rest_framework.filters import OrderingFilter

from django.shortcuts import get_object_or_404

from django_filters.rest_framework import DjangoFilterBackend

from .serializers import PostSerializer
from ...services import get_likes_stats
from ...paginators import DefaultPagePaginator
from ...permissons import IsAuthor
from ...models import Post, Like
from ...filters import DateFilter


class ListCreatePostView(ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly, )

    pagination_class = DefaultPagePaginator

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

    filter_backends = [DateFilter]
    date_fields = ['date']

    def get(self, request, pk):
        post: Post = get_object_or_404(Post, pk=pk)
        self.check_object_permissions(self.request, post)

        post_likes = Like.objects.filter(post=post)
        post_likes = self.filter_queryset(post_likes)

        stats = get_likes_stats(post_likes)

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
