from django.urls import path
from .views import ProfileListView
app_name = 'users'
urlpatterns = [
    path('', ProfileListView.as_view(), name='profiles')
]
