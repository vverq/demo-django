from django.contrib import admin

from .models import Comment, Post, Ip


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'text')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'text')


@admin.register(Ip)
class IpAdmin(admin.ModelAdmin):
    list_display = ('id', 'ip', 'post')
