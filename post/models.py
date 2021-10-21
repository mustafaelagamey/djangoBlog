from django.core.validators import MinLengthValidator
from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils.text import slugify


class Post(models.Model):
    creation_datetime = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=250)
    content = models.TextField(validators=[MinLengthValidator(10)])
    slug = models.SlugField(default="", null=False, unique=True)
    author = models.ForeignKey('Author', null=True, on_delete=models.SET_NULL)
    tags = models.ManyToManyField('Tag')
    image = models.ImageField(default=None, null=True, upload_to='posts_images')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(args, kwargs)

    def get_absolute_url(self):
        return reverse(viewname='post:view', kwargs={'slug': self.slug})


class Author(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    slug = models.SlugField(default="", null=False, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.first_name} {self.last_name}")
        return super(Author, self).save()

    def get_absolute_url(self):
        return reverse('post:author-view', kwargs={'slug': self.slug})

    def __str__(self):
        return self.full_name()

    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class Tag(models.Model):
    caption = models.CharField(max_length=30)

    def __str__(self):
        return self.caption
