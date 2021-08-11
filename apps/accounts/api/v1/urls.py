from django.urls import path, include

from .views import RetrieveUserView

urlpatterns = [
    path('', include('dj_rest_auth.urls')),
    path('user/<int:pk>/', RetrieveUserView.as_view()),
    path('register/', include('dj_rest_auth.registration.urls')),
]