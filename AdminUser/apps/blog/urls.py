from django.contrib import admin
from django.urls import path, include
from .views import BlogListView, BlogDetailView, post_new

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post'),
    path('post/new/', post_new, name='post_new'),
]