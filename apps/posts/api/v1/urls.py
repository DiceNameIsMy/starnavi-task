from django.urls import path

from .views import (
    LikePostView, 
    ListCreatePostView, 
    RetrieveUpdateDestroyPostView,
    PostStatsView
)

urlpatterns = [
    path('', ListCreatePostView.as_view(), 
        name='create_list_post'
    ),
    path('<int:pk>/', RetrieveUpdateDestroyPostView.as_view(), 
        name='retireve_update_destroy_post_view'
    ),
    path('<int:pk>/stats/', PostStatsView.as_view(), name='post_stats_view'),
    path('<int:pk>/like/', LikePostView.as_view(), name='like_post'),
]