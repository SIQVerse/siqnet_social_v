from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect
from .models import Profile

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
