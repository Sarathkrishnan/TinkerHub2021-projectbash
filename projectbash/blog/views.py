from django.shortcuts import render, get_object_or_404
from .models import Article, Author

# Create your views here.
def index(request):
    no_of_blogs= Article.objects.all().count
    blogs=Article.objects.all()
    context={
        'no_of_blogs':no_of_blogs,
        'blogs':blogs,
    }
    return render(request,'index.html',context=context)

def blogView(request,blog_id):
    context={
        'blog':get_object_or_404(Article,pk=blog_id)}
    return render(request,'blog.html',context=context)

def blogger(request, blogger_id):
    author=get_object_or_404(Author,pk=blogger_id)
    context={
        'author':author,
        'blogs':Article.objects.filter(author=author.user.username)
    }
    return render(request,'author.html',context=context)