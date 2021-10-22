from django.urls import path
from . import views
from .views import LandingPageView, PostListView, PostDetailView, AuthorDetailView, CommentView

app_name = 'post'
urlpatterns = [
    path('', LandingPageView.as_view(), name='landing-page'),
    path('post', PostListView.as_view(), name='list'),
    path('post/<slug>', PostDetailView.as_view(), name='detail'),
    path('author/<slug>', AuthorDetailView.as_view(), name='author-detail'),
    path('post/<slug>/comment', CommentView.as_view(), name='comment'),

]
