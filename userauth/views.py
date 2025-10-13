from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def edit_profile(request):
    user = request.user
    profile = user.profile

    if request.method == 'POST':
        # Update bio
        profile.bio = request.POST.get('bio', profile.bio)

        # Update avatar if uploaded
        if 'avatar' in request.FILES:
            profile.avatar = request.FILES['avatar']

        # Update banner if uploaded
        if 'banner' in request.FILES:
            profile.banner = request.FILES['banner']

        profile.save()
        return redirect('profile')  # Redirect to the profile view

    return render(request, 'userauth/edit_profile.html', {'user': user})
