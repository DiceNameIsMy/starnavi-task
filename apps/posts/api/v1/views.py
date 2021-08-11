from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED ,HTTP_204_NO_CONTENT

from django.shortcuts import get_object_or_404

from ...models import Post


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
