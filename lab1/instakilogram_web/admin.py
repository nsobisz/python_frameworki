from django.contrib import admin
from .models import Post, Insta_users

# Register your models here.

admin.site.register(Insta_users)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    fields = ["content", "imgThumb", "author"]
    list_display = ["post_ID", "date"]
    list_filter = ["date"]
    search_fields = ["post_ID", "date"]
