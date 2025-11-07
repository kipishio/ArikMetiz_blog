"""Определяет схемы URL для blogs."""

from django.urls import path
from . import views

app_name = 'blogs'

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/', views.posts, name='posts'),
    path('myposts/', views.myposts, name='myposts'),
    path('post/<int:post_id>/', views.post, name='post'),
    path('addpost/', views.addpost, name='addpost'),
    path('editpost/<int:post_id>/', views.editpost, name='editpost'),
]
