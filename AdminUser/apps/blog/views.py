from django.views.generic import ListView, DetailView
from .models import Post


class BlogListView(ListView):
    model = Post
    template_name = 'main/home.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'main/post.html'