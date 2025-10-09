from django.contrib import admin
from django.urls import path, include
from userauth.views import home

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('userauth/', include('userauth.urls')),
    path('versnet/', include('versnet.urls')),
]
