from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm


class BlogListView(ListView):
    model = Post
    template_name = 'main/home.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'main/post.html'


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post', pk=post.pk)
    form = PostForm()
    return render(request, 'main/post_edit.html', {'form': form})