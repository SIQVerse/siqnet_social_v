from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.core.mail import send_mail

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
    path('test-email/', test_email, name='test_email'),  # ← This is the line you're asking about
]
