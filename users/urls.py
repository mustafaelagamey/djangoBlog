from django.urls import path
from .views import ProfileListView, ProfileDetailView

app_name = 'users'
urlpatterns = [
    path('profiles', ProfileListView.as_view(), name='profile-list'),
    path('profiles/<pk>', ProfileDetailView.as_view(), name='profile-detail'),
]
