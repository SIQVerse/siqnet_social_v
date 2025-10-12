from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("SIQNet Social V is live!")

urlpatterns = [
    path('', home, name='home'),  # Root URL
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
]

