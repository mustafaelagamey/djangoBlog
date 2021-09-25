from django.urls import path
from . import views

urlpatterns = [
    path('', views.latest),
    path('posts', views.listing),
    path('post/<title>', views.view),
]
