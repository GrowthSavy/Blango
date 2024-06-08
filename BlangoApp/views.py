from django.shortcuts import render
from django.http import Http404
# Create your views here.
from .models import Post
from django.shortcuts import get_object_or_404

def PostListView(request):
    posts = Post.published.all()
    return render(request,template_name="blog/post/list.html",context={'posts':posts})

def PostDetailView(request,id):
    post = Post.published.get_object_or_404(Post,id=id,status= Post.Status.PUBLISH)
    
    return render(request, template_name="blog/post/detail.html",context={'post':post})