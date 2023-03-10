from django.shortcuts import render, redirect, get_object_or_404
from .models import Post

def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})

def create_post(request):
    post_text = request.POST['post_text']
    post = Post(post_text=post_text, author=request.user)
    post.save()
    return redirect('/')

def post_details(request, id):
    post = get_object_or_404(Post, pk=id)
    return render(request, 'detail.html', {'post':post})