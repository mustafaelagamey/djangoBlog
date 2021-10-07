from django.contrib import admin
from django.utils.text import slugify

from .models import Post, Author


# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('title',)
    prepopulated_fields = {'slug': ('title',)}


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Post, PostAdmin)

admin.site.register(Author, AuthorAdmin)
