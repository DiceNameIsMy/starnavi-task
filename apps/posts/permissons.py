from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAuthor(BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.author == request.user:
            return True

class IsAuthorOrReadOnly(BasePermission):
    message = 'you are not allowed to change not your posts'

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        if obj.author == request.user:
            return True
