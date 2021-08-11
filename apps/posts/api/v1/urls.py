from django.urls import path

from .views import LikePostView, ListCreatePostView, RetrieveUpdateDestroyPostView

urlpatterns = [
    path('', ListCreatePostView.as_view(), 
        name='create_list_post'
    ),
    path('<int:pk>/', RetrieveUpdateDestroyPostView.as_view(), 
        name='retireve_update_destroy_post_view'
    ),
    path('', ListCreatePostView.as_view(), name='create_list_post'), # All posts with filters
    path('<int:pk>/like/', LikePostView.as_view()),
]