from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('userauth/', include('userauth.urls')),
    path('userposts/', include('userposts.urls')),
    path('community/', include('community.urls')),
    path('siqposts/', include('siqposts.urls')),
    path('versnet/', include('versnet.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
