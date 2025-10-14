from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Post, Comment, Like

def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'siqposts/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all().order_by('-created_at')

    if request.method == 'POST':
        content = request.POST.get('content')
        if content and request.user.is_authenticated:
            Comment.objects.create(post=post, author=request.user, content=content)
            return HttpResponseRedirect(reverse('post_detail', args=[pk]))

    return render(request, 'siqposts/post_detail.html', {'post': post, 'comments': comments})

def toggle_like(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user.is_authenticated:
        like, created = Like.objects.get_or_create(post=post, user=request.user)
        if not created:
            like.delete()
    return HttpResponseRedirect(reverse('post_detail', args=[pk]))
