from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Post, Comment, Like, Profile

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

def profile_view(request, username):
    user = get_object_or_404(User, username=username)
    profile = user.profile
    is_following = request.user.profile.following.filter(pk=profile.pk).exists()
    return render(request, 'siqposts/profile.html', {
        'profile_user': user,
        'profile': profile,
        'is_following': is_following
    })

def follow_user(request, username):
    target_user = get_object_or_404(User, username=username)
    profile = request.user.profile
    profile.following.add(target_user.profile)
    return redirect('profile', username=username)

def unfollow_user(request, username):
    target_user = get_object_or_404(User, username=username)
    profile = request.user.profile
    profile.following.remove(target_user.profile)
    return redirect('profile', username=username)

def search_posts(request):
    query = request.GET.get('q')
    results = Post.objects.filter(title__icontains=query) if query else []
    return render(request, 'siqposts/search_results.html', {'results': results, 'query': query})
