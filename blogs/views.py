from django.shortcuts import render, redirect
from .models import BlogPost
from .forms import BlogPostForm
from django.contrib.auth.decorators import login_required


def index(request):
    """Домашняя страница приложения Learning Log"""
    return render(request, 'blogs/index.html')


def posts(request):
    """Список всех статей блога"""
    blog_posts = BlogPost.objects.order_by('-date_added')
    context = {'blog_posts': blog_posts}
    return render(request, 'blogs/posts.html', context)


def myposts(request):
    """Список всех статей блога"""
    blog_posts = BlogPost.objects.filter(owner=request.user).order_by('-date_added')
    context = {'blog_posts': blog_posts}
    return render(request, 'blogs/myposts.html', context)


def post(request, post_id):
    """Список всех статей блога"""
    # если поста нет с id то выводит список всех постов
    try:
        post = BlogPost.objects.get(id=post_id)
    except BlogPost.DoesNotExist:
        return redirect('blogs:posts')

    context = {'post': post}
    return render(request, 'blogs/post.html', context)


@login_required
def addpost(request):
    """Добавление в блог нового поста"""
    if request.method != 'POST':
        form = BlogPostForm()
    else:
        form = BlogPostForm(data=request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.owner = request.user
            form.save()
            return redirect('blogs:posts')

    context = {'form': form}
    return render(request, 'blogs/addpost.html', context)


@login_required
def editpost(request, post_id):
    """Редактируем запись поста в блоге"""

    # проверяем принадлежит ли пост который собираемся редактировать пользователю.
    try:
        post = BlogPost.objects.get(id=post_id)
    except BlogPost.DoesNotExist:
        return redirect('blogs:myposts')
    if post.owner != request.user:
        return redirect('blogs:myposts')

    if request.method != 'POST':
        form = BlogPostForm(instance=post)
    else:
        form = BlogPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blogs:post', post_id=post_id)

    context = {'post': post, 'form': form}
    return render(request, 'blogs/editpost.html', context)
