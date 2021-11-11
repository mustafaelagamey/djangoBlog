from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class ProfileListView(TemplateView):
    template_name = 'users/profile/list.html'
