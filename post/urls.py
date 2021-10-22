from django.urls import path
from . import views
from .views import LandingPageView

app_name = 'post'
urlpatterns = [
    path('', LandingPageView.as_view(), name='landing-page'),
    path('post', views.listing, name='listing'),
    path('post/<slug>', views.view, name='view'),
    path('author/<slug>', views.author_view, name='author-view'),
]
