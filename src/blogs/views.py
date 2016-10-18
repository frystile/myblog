from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.

class PostList(ListView):
    template_name = "blogs/post_list.html"
    model = Post

class PostDetail(DetailView):
    model = Post
