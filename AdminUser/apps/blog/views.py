from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Post, Category
from .forms import PostForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def home_page(request, posts, categories):
    paginator = Paginator(posts, 6)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'main/home.html', {'posts': posts, 'categories': categories, 'page': page})


def post_list(request):
    categories = Category.objects.all()
    posts = Post.objects.filter(pub_date__lte=timezone.datetime.now()).order_by('-pub_date')
    return home_page(request, posts, categories)


def post_list_by_category(request, pk):
    categories = Category.objects.all()
    category = get_object_or_404(Category, pk=pk)
    posts = Post.objects.filter(category=category).order_by('-pub_date')
    return home_page(request, posts, categories)


def user_posts(request):
    user = request.user
    posts = Post.objects.filter(pub_date__lte=timezone.datetime.now(), author=user).order_by('-pub_date')
    paginator = Paginator(posts, 6)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'main/user_posts.html', {'posts': posts, 'page': page})


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


def post_del(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.author == request.user:
        post.delete()
    return redirect('home')


def post_edit(request, pk):
    if pk:
        post = get_object_or_404(Post, pk=pk)
        if post.author != request.user:
            return redirect('post', pk=post.pk)
    else:
        post = Post(author=request.user)

    form = PostForm(request.POST or None, instance=post)
    if request.POST and form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'main/post_edit.html', {'form': form})