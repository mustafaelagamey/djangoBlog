from django.core.validators import MinLengthValidator
from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils.text import slugify

from users.models import Profile


class Post(models.Model):
    creation = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=250)
    content = models.TextField(validators=[MinLengthValidator(10)])
    slug = models.SlugField(default="", null=False, unique=True)
    author = models.ForeignKey(Profile, null=True, on_delete=models.SET_NULL)
    tags = models.ManyToManyField('Tag')
    image = models.ImageField(default=None, null=True, upload_to='posts_images')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(args, kwargs)

    def get_absolute_url(self):
        return reverse(viewname='posts:detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.slug


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
        return reverse('posts:author-detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.full_name()

    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class Tag(models.Model):
    caption = models.CharField(max_length=30)

    def __str__(self):
        return self.caption


class Comment(models.Model):
    commenter = models.CharField(max_length=20)
    commenter_email = models.EmailField(max_length=80)
    text = models.TextField(max_length=500)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.text[:20]} | {self.commenter} | {self.post.slug}"
