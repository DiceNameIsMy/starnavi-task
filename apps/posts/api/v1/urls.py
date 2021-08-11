from django.urls import path

from .views import LikePostView, ListCreatePostView

urlpatterns = [
    path('', ListCreatePostView.as_view(), name='create_list_post'), # All posts with filters
    path('<int:pk>/like/', LikePostView.as_view()),
]