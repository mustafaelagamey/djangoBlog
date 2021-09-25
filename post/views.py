from django.http import HttpResponse
from .dummy_posts import post_list
from django.shortcuts import render


# Create your views here.


def latest(request):
    context = {
        'posts': post_list[:3]
    }
    return render(request, 'post/latest.html', context)


def listing(request):
    context = {
        'posts': post_list[:4]
    }
    return render(request, 'post/list.html', context)


def view(request, title):
    posts = [post for post in post_list if post.get('title') == title]
    context = {
        'post': posts[0]
    }
    return render(request, 'post/view.html', context)
