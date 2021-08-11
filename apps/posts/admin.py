from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'author', 'id', 'count_likes')
    fields = ('author', 'image', 'text', 'count_likes')
    readonly_fields = ('count_likes', )
