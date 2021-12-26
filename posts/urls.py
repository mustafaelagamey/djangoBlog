from django.urls import path
from . import views
from .views import LandingPageView, PostListView, PostDetailView, AuthorDetailView, CommentView, ReadLaterView, \
    PostCreateView

app_name = 'posts'
urlpatterns = [
    path('', LandingPageView.as_view(), name='landing-page'),
    path('post', PostListView.as_view(), name='list'),
    path('post/saved-posts', ReadLaterView.as_view(), name='saved-posts'),
    path('post/<slug>', PostDetailView.as_view(), name='detail'),
    path('post/create/', PostCreateView.as_view(), name='create'),
    path('author/<slug>', AuthorDetailView.as_view(), name='author-detail'),
    path('post/<slug>/comment', CommentView.as_view(), name='comment'),
    path('post/<slug>/read-later', ReadLaterView.as_view(), name='read-later'),
]
