from django.contrib import admin
from django.utils.text import slugify

from .models import Post, Author, Tag, Comment


# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('title',)
    prepopulated_fields = {'slug': ('title',)}


class AuthorAdmin(admin.ModelAdmin):
    # list_display = ('name',)
    prepopulated_fields = {'slug': ('first_name', 'last_name')}


admin.site.register(Post, PostAdmin)

admin.site.register(Author, AuthorAdmin)
admin.site.register(Tag)


class CommentAdmin(admin.ModelAdmin):
    def shorten_text(self, comment):
        return comment.text[:50]

    def post_slug(self, comment):
        return comment.post.slug

    list_display = ('commenter', 'post_slug', 'shorten_text')


admin.site.register(Comment, CommentAdmin)
