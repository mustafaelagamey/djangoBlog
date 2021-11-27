from django.contrib.auth.models import User
from django.db import models

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    username = models.CharField(max_length=20)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    email = models.EmailField()
    title = models.CharField(max_length=80, null=True)
    address = models.CharField(max_length=200, null=True)
    short_intro = models.CharField(max_length=200, null=True, blank=True)
    bio = models.TextField(blank=True, null=True)
    profile_image = models.ImageField(null=True, blank=True, upload_to='profiles_images')

    def __str__(self):
        return self.username

    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"


#   to add signal by two ways:
#       - declare function and assign it to the trigger
#       - use receiver decorator and set the trigger and sender if required
# def receiver_fn(sender,instance,created **kwargs): pass
# trigger.connect (fn , sender = ModelName)
#  or @receiver(trigger, sender=ModelName) for the receiver_fn

def create_profile(sender, instance: User, created, **kwargs):
    if created or not hasattr(instance, 'profile'):
        profile = Profile()
    else:
        profile = instance.profile
    set_attrs(instance, profile, ['username', 'first_name', 'last_name', 'email'])
    profile.user = instance
    profile.save()


def set_attrs(src: object, dst: object, user_fields: list):
    for key in user_fields:
        setattr(dst, key, getattr(src, key))


post_save.connect(create_profile, sender=User)


@receiver(post_delete, sender=Profile)
def delete_user(sender, instance, **kwargs):
    from django.core.exceptions import ObjectDoesNotExist
    try:
        if hasattr(instance, 'user') and instance.user:
            instance.user.delete()
    except ObjectDoesNotExist as e:
        pass
