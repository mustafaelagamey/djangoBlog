from django.contrib import admin
from django.utils.text import slugify

from .models import Post


# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('title',)
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Post, PostAdmin)
