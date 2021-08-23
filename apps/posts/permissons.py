from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAuthor(BasePermission):
    """ `user_permisson_filed` is required in view
    """
    message = 'you are not allowed to view this object'

    def has_object_permission(self, request, view, obj):
        if getattr(obj, view.user_permisson_field) == request.user:
            return True

class IsAuthorOrReadOnly(BasePermission):
    """ `user_permisson_filed` is required in view
    """
    message = 'you are not allowed to change not your object'

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        if getattr(obj, view.user_permisson_field) == request.user:
            return True
