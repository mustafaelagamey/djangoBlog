from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField( max_length=150, blank=True)
    last_name = models.CharField( max_length=150, blank=True)
    email = models.EmailField( blank=True)
    short_intro = models.CharField(max_length=200 , null=True , blank=True)
    bio = models.TextField(blank=True , null=True)
    profile_image = models.ImageField(null=True, blank=True, upload_to='profiles_images')

    def __str__(self):
        return str(self.email)

