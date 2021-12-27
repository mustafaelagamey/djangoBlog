from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, FormView

from .forms import LoginForm
from .models import Profile


class ProfileListView(ListView):
    template_name = 'users/profile/list.html'
    model = Profile


class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'users/profile/detail.html'


class LoginView(FormView):
    form_class = LoginForm
    template_name = 'users/login.html'
    success_url = reverse_lazy('posts:landing-page')

    def get_success_url(self):
        if self.request.GET.get('next'):
            return self.request.GET['next']
        else:
            return self.success_url

    def form_valid(self, form):
        user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
        if user:
            login(self.request, user)
        else:
            messages.error(self.request, "Invalid Credentials")
            return self.form_invalid(form)
        return super(LoginView, self).form_valid(form)


def log_user_out(request):
    logout(request)
    return redirect('login')
