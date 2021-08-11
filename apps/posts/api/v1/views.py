from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED ,HTTP_204_NO_CONTENT
from rest_framework.filters import OrderingFilter

from django.shortcuts import get_object_or_404

from .serializers import PostSerializer
from ...models import Post
from ...filters import DateFilter


class ListCreatePostView(ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly, )

    filter_backends = [OrderingFilter, DateFilter]
    ordering = ['created_at', 'updated_at' ]
    date_fields = ['created_at', 'updated_at']

    queryset = Post.objects.all()
    serializer_class = PostSerializer



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
