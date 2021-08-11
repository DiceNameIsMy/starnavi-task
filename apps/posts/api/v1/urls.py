from django.urls import path

from .views import LikePostView

urlpatterns = [
    path('<int:pk>/like/', LikePostView.as_view()),
]