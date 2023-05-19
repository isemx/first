from django.shortcuts import render
from .models import Blog
from django.db import models
from django.views.generic import ListView

def blog(request):
    post = Blog.objects.all()
    return render(request, 'blog/blog.html', {'post': post})

# Create your views here.
