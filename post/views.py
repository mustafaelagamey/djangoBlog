from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import ListView

from .models import Post, Author


# Create your views here.


class LandingPageView(ListView):
    template_name = 'post/landing_page.html'
    model = Post
    context_object_name = 'posts'
    ordering = ['-creation_datetime']

    def get_queryset(self):
        query_set = super(LandingPageView, self).get_queryset()
        return query_set[:3]


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
