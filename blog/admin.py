from django.contrib import admin
from .models import Post ,Comment
from django.utils.text import slugify

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'published', 'post_date']
    list_filter = ['published','post_date', 'updated']
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}


class CommentAdmin(admin.ModelAdmin):
    pass



admin.site.register(Post, PostAdmin)
admin.site.register(Comment,CommentAdmin)
