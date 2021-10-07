from django.http import HttpResponse, Http404
from django.shortcuts import render
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
    try:
        context = {
            'post': Post.objects.get(slug=slug)
        }
    except (Post.DoesNotExist, Post.MultipleObjectsReturned) as e:
        raise Http404
    return render(request, 'post/view.html', context)


def author_view(request, slug):
    try:
        context = {
            'author': Author.objects.get(slug=slug)
        }
    except (Author.DoesNotExist, Author.MultipleObjectsReturned) as e:
        raise Http404

    return render(request, 'author/view.html', context)
