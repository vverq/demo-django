from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:post_id>', views.post, name="post"),
    path('post/<int:post_id>/create_comment', views.create_comment, name="create_comment"),
    path("create_post/", views.create_post, name="create_post"),
]