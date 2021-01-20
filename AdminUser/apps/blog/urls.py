from django.contrib import admin
from django.urls import path, include
from .views import BlogDetailView, post_new, post_list, post_list_by_category, user_posts, post_del, post_edit

urlpatterns = [
    path('', post_list, name='home'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post'),
    path('post/new/', post_new, name='post_new'),
    path('post/edit/<int:pk>/', post_edit, name='post_edit'),
    path('post/del/<int:pk>/', post_del, name='post_del'),
    path('category/<int:pk>/', post_list_by_category, name='post_by_category'),
    path('post/my/', user_posts, name='user_posts')
]