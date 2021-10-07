from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils.text import slugify


class Post(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    slug = models.SlugField(default="", null=False, unique=True)
    author = models.ForeignKey('Author', null=True, on_delete=models.SET_NULL)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(args, kwargs)

    def get_absolute_url(self):
        return reverse(viewname='post:view', kwargs={'slug': self.slug})


class Author(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(default="", null=False, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super(Author, self).save()

    def get_abolute_url(self):
        return reverse('post:author-view', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name
