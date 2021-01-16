"""projectbash URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from blog.views import BlogsListView, blogView, author, bloggers, addblog, add_comment


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', BlogsListView.as_view(), name='blogs_list'),
    path('blog/<int:pk>/', blogView, name='blog-view'),
    path('blogger/<int:pk>', author, name='author'),
    path('blogers', bloggers, name='bloggers'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('add/', addblog, name='addblog'),
    path('add_comment/',add_comment, name='CommentForm')
   
]
