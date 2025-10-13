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
    'allauth.socialaccount.providers.google',  # or Facebook, GitHub, etc.
]
