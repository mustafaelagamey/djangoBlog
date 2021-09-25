from django.urls import path
from . import views

app_name = 'post'
urlpatterns = [
    path('', views.latest, name='latest'),
    path('post', views.listing, name='listing'),
    path('post/<title>', views.view, name='view'),
]
