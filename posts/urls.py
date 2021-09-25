from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.latest, name='latest'),
    path('posts', views.listing, name='listing'),
    path('post/<title>', views.view, name='view'),
]
