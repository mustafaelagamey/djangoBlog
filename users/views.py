from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, ListView, DetailView

from .models import Profile


class ProfileListView(ListView):
    template_name = 'users/profile/list.html'
    model = Profile


class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'users/profile/detail.html'
