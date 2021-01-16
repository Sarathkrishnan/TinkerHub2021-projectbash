from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date
# Create your models here.

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL,null=True)

    class Meta:
        ordering=["user"]
    
    def get_absolute_url(self):
        return reverse('blogs-by-author',args=[str(self.id)])
    def __str__(self):
        return self.user.username


class Article(models.Model):
    name=models.CharField(max_length=100)
    content=models.CharField(max_length=1500,)
    publishing_date=models.DateField(default=date.today)
    author=models.ForeignKey(Author, on_delete=models.SET_NULL,null=True)

    class Meta:
        ordering=["-publishing_date"]
    
    def get_absolute_url(self):
         return reverse('blog-view',args=[str(self.id)])
    
    def __str__(self):
        return self.name

class Comment(models.Model):
    comment_text=models.CharField(max_length=200)
    person=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    date=models.DateField(auto_now_add=True)
    article=models.ForeignKey(Article,on_delete=models.CASCADE)

    class Meta:
        ordering=['date']
    
    def __str__(self):
        return self.comment_text