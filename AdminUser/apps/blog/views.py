from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Post, Category
from .forms import PostForm


def post_list(request):
    categories = Category.objects.all()
    posts = Post.objects.filter(pub_date__lte=timezone.datetime.now()).order_by('-pub_date')

    return render(request, 'main/home.html', {'posts': posts, 'categories': categories})


def post_list_by_category(request, pk):
    categories = Category.objects.all()
    category = get_object_or_404(Category, pk=pk)
    posts = Post.objects.filter(category=category).order_by('-pub_date')
    return render(request, 'main/home.html', {'posts': posts, 'categories': categories})


class BlogDetailView(DetailView):
    model = Post
    template_name = 'main/post.html'


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.pub_date = timezone.datetime.now()
            post.save()
            return redirect('post', pk=post.pk)
    form = PostForm()
    return render(request, 'main/post_edit.html', {'form': form})