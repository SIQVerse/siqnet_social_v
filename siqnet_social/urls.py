from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.conf.urls.static import static

def home(request):
    return HttpResponse("SIQNet Social V is live!")

def test_email(request):
    send_mail(
        'SIQNet Email Test',
        'This is a test email from SIQNet Social V.',
        'smlzulu@gmail.com',
        ['smlzulu@gmail.com'],
        fail_silently=False,
    )
    return HttpResponse("Email sent!")

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('posts/', include('siqposts.urls')),       # ✅ Community feed
    path('profiles/', include('userposts.urls')),   # ✅ Optional: user profiles
    path('test-email/', test_email, name='test_email'),
]

# ✅ Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
