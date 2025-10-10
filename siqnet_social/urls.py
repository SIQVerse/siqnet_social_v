# siqnet_social/urls.py

from django.contrib import admin
from django.urls import path, include
from userauth import views as userauth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', userauth_views.home, name='home'),

    # ✅ Auth routes
    path('accounts/', include('accounts.urls')),
]
