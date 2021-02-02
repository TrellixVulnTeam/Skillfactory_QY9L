# from django.shortcuts import render
from django.views.generic import ListView, DetailView
#from datetime import datetime

from .models import Author, Post, Comment
class PostsList(ListView):
    model = Post
    template_name = 'posts.html'
    context_object_name = 'posts'
    queryset = Post.objects.order_by('-create_date')


class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'