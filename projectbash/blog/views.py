from django.shortcuts import render
from .models import Article
# Create your views here.
def index(request):
    no_of_blogs= Article.objects.all().count
    blogs=Article.objects.all()
    context={
        'no_of_blogs':no_of_blogs,
        'blogs':blogs,
    }
    return render(request,'index.html',context=context)

