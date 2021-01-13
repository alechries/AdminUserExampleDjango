from django.contrib import admin
from django.urls import path, include
from .views import BlogDetailView, post_new, post_list, post_list_by_category

urlpatterns = [
    path('', post_list, name='home'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post'),
    path('post/new/', post_new, name='post_new'),
    path('category/<int:pk>/', post_list_by_category, name='post_by_category'),

]