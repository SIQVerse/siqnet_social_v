from django.contrib import admin
from django.urls import path
from userauth import views  # Update this if your homepage view is in a different app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Make sure 'home' exists in userauth/views.py
]
