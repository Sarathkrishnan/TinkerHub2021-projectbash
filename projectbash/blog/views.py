from django.shortcuts import render, Http404, get_object_or_404, redirect
from django.views import generic
from .models import Article, Author, Comment
from .forms import AddblogForm, CommentForm
from django.utils import timezone


# Create your views here.


class BlogsListView(generic.ListView):
    model = Article
    paginate_by = 4
    context_object_name = 'blogs_list'
    queryset = Article.objects.all()[:5]
    template_name = 'index.html'

    def get_queryset(self):
        return Article.objects.all()[:5]

    def get_context_date(self, **kwargs):
        context = super(BlogsListView, self).get_context_date(**kwargs)
        context['some_data'] = 'This is just some data'
        return context


def blogView(request, pk):
    blog=get_object_or_404(Article, pk=pk)
    comments=Comment.objects.filter(article=blog)
    context = {
        'blog': blog,
        'comments':comments
        }
    return render(request, 'blog.html', context=context)


def author(request, pk):
    blogs=Article.objects.filter(author__id=pk)
    context = {
        'author': get_object_or_404(Author, pk=pk),
        'blogs': blogs
    }
    return render(request, 'author.html', context=context)


def bloggers(request):
    context = {
        'bloggers': Author.objects.all()
    }
    return render(request, 'blogger.html', context=context)


def addblog(request):
    if request.method == 'POST':
        form = AddblogForm(request.POST)
        if form.is_valid:
            post = form.save(commit=False)
            #post.author = Author.objects.get(name__contains=request.user.username)
            post.published_date = timezone.now()
            post.save()
            return redirect('blog-view', pk=post.pk)
    else:
        form = AddblogForm()
    return render(request, 'addpost.html', {'form': form})

    


def add_comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid:
            post = form.save(commit=False)
            
            post.published_date = timezone.now()
        
            post.save()
            return redirect('blog-view', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'comment.html', {'form': form})
