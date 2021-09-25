from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.


def latest_posts(request):
    return render(request,'posts/latest_posts.html')
