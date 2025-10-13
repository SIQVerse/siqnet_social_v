from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    user = request.user
    campaigns = user.profile.campaigns.order_by('-impact_score')  # or use '-date_joined'

    return render(request, 'userauth/profile.html', {
        'user': user,
        'campaigns': campaigns
    })
