from django.db import models
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Post
# Create your views here.

class PostListView(ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog-post-list.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'post-detail.html'