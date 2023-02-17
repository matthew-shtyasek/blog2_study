from django.contrib import admin

from posts.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    readonly_fields = ("publish_date", "change_date", "likes")
    list_display = ("title", "publish_date", "change_date", "author", "published")
    search_fields = ("title", "text")
    list_filter = ("publish_date", "change_date", "published")