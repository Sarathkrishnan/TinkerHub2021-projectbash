from django.contrib import admin
from .models import Author,Comment, Article
# Register your models here.

admin.site.register(Author)
admin.site.register(Article)
admin.site.register(Comment)