from django.contrib import admin
from django.urls import path
from userauth import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
]
