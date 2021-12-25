from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
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

    def form_valid(self, form):
        user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
        if not user :
            raise Exception("Invalid Credentials")
        login(self.request, user)
        return super(LoginView, self).form_valid(form)


class LogoutView(View):
    def get(self, request):
        logout(self.request)
        return redirect('login')
