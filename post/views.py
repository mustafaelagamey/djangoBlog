from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView

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


class PostListView(ListView):
    template_name = 'post/list.html'
    context_object_name = 'posts'
    model = Post
    ordering = ['-creation_datetime']


class PostDetailView(DetailView):
    model = Post
    template_name = 'post/detail.html'

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context.update(post_tags=self.object.tags.all())
        return context


def author_view(request, slug):
    context = {
        'author': get_object_or_404(Author.objects, slug=slug)
    }

    return render(request, 'author/view.html', context)
