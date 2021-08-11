from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include([

        path('v1/', include([
            path('accounts/', include('apps.accounts.api.v1.urls')),
            path('posts/', include('apps.posts.api.v1.urls')),
        ]))

    ]))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

