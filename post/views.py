from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .models import Post, Author


# Create your views here.


def latest(request):
    context = {
        'posts': Post.objects.all().order_by('-creation_datetime')[:3]
    }
    return render(request, 'post/latest.html', context)


def listing(request):
    context = {
        'posts': Post.objects.all()[:4]
    }
    return render(request, 'post/list.html', context)


def view(request, slug):
    posts = get_object_or_404(Post.objects, slug=slug)
    context = {
        'post': posts,
        'post_tags': posts.tags.all()
    }
    return render(request, 'post/view.html', context)


def author_view(request, slug):
    context = {
        'author': get_object_or_404(Author.objects, slug=slug)
    }

    return render(request, 'author/view.html', context)
