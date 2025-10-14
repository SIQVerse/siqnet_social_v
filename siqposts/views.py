from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Post, Comment, Like, Profile, Notification, Message, Tag

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
            Notification.objects.create(
                recipient=post.author,
                message=f"{request.user.username} commented on your post."
            )
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
    Notification.objects.create(
        recipient=target_user,
        message=f"{request.user.username} started following you."
    )
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

@login_required
def create_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        image = request.FILES.get('image')
        if title and content:
            post = Post.objects.create(author=request.user, title=title, content=content, image=image)

            # Handle tags
            tag_names = request.POST.get('tags', '').split(',')
            for name in tag_names:
                name = name.strip()
                if name:
                    tag, _ = Tag.objects.get_or_create(name=name)
                    post.tags.add(tag)

            return redirect('post_list')
    return render(request, 'siqposts/create_post.html')

@login_required
def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk, author=request.user)
    if request.method == 'POST':
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.image = request.FILES.get('image')
        post.save()

        # Update tags
        post
