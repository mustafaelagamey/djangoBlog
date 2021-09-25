from django.http import HttpResponse
from .dummy_posts import posts_list
from django.shortcuts import render


# Create your views here.


def latest_posts(request):
    context = {
        'posts': posts_list[:3]
    }
    return render(request,'posts/latest_posts.html',context)
