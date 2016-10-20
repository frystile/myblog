from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *

# Create your views here.

class PostList(DetailView):
    template_name = "blogs/post_list.html"
    model = Blog

#    def get_queryset(self):
#        return Post.objects.filter(blog__id=PostList.pk)

class PostDetail(DetailView):
    template_name = "blogs/post_detail.html"
    model = Post

class BlogList(ListView):
    template_name = "blogs/blog_list.html"
    model = Blog
