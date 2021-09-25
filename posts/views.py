from django.http import HttpResponse
from .dummy_posts import posts_list
from django.shortcuts import render


# Create your views here.


def latest(request):
    context = {
        'posts': posts_list[:3]
    }
    return render(request, 'posts/latest.html', context)


def listing(request):
    context = {
        'posts': posts_list[:4]
    }
    return render(request, 'posts/list.html', context)
