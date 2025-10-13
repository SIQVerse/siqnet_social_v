# settings.py

# Core Django settings
INSTALLED_APPS = [
    # Django core apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',  # Required for django-allauth

    # Your custom apps
    'accounts',
    'siqposts',
    'userposts',
    'versnet',

    # Add-ons and integrations
    'rest_framework',
    'crispy_forms',
    'django_extensions',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',  # Add more providers as needed
]

# Site ID for django-allauth
SITE_ID = 1

# Crispy Forms config
CRISPY_TEMPLATE_PACK = 'bootstrap4'  # Or 'bootstrap5' if you're using it

# Authentication backends
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

# Allauth settings
LOGIN_REDIRECT_URL = '/'  # Redirect after login
ACCOUNT_EMAIL_VERIFICATION = 'optional'  # Can be 'mandatory'
ACCOUNT_EMAIL_REQUIRED = True

# Static and media files
STATIC_URL = '/static/'
MEDIA_URL = '/media/'

# Add these if deploying with Whitenoise
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Database config (example using dj-database-url)
import dj_database_url
DATABASES = {
    'default': dj_database_url.config(default='sqlite:///db.sqlite3')
}

# Security and debug
DEBUG = False  # Set to True in development
ALLOWED_HOSTS = ['yourdomain.com', 'localhost', '127.0.0.1']
SECRET_KEY = 'your-secret-key'  # Use environment variable in production
