from django.http import HttpResponse, Http404
from django.views import View
from django.views.generic import ListView, DetailView

from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import FormView

from .models import Post, Author
from .forms import CommentForm


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
        context.update(post_tags=self.object.tags.all(), comment_form=CommentForm())

        return context


class AuthorDetailView(DetailView):
    model = Author
    template_name = 'author/detail.html'


class CommentView(View):
    def post(self,request,slug):
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('post:detail', slug=slug)

    def get(self, request, slug):
        raise Http404
