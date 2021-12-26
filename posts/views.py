from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.views import View
from django.views.generic import ListView, DetailView, CreateView

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
    ordering = ['-creation']

    def get_queryset(self):
        query_set = super(LandingPageView, self).get_queryset()
        return query_set[:3]


class PostListView(ListView):
    template_name = 'post/list.html'
    context_object_name = 'posts'
    model = Post
    ordering = ['-creation']


class PostDetailView(DetailView):
    model = Post
    template_name = 'post/detail.html'

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context.update(post_tags=self.object.tags.all(), comment_form=CommentForm())

        return context


class PostCreateView(CreateView):
    model = Post
    template_name = 'post/create.html'
    fields = '__all__'


class AuthorDetailView(DetailView):
    model = Author
    template_name = 'author/detail.html'


class CommentView(View):
    def post(self, request, slug):
        form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            context = {
                'comment_form': form,
                'post': post
            }
            return render(request, 'post/detail.html', context=context)
        return redirect('posts:detail', slug=slug)

    def get(self, request, slug):
        raise Http404


class ReadLaterView(View):
    def get(self, request):
        print(request.session.get('read_later', []))
        posts = Post.objects.filter(slug__in =  request.session.get('read_later', []))
        context = {
            'posts': posts
        }
        return render(request, 'post/list.html', context=context)

    def post(self, request, slug):
        read_later = request.session.setdefault('read_later', [])
        print(slug)
        print(read_later)
        if int(request.POST.get('read_later', 0)):
            read_later.append(slug)
        else:
            if slug in read_later:
                read_later.remove(slug)
        request.session.modified = True
        print(request.POST)
        return HttpResponseRedirect(request.POST.get('next', '/'))
