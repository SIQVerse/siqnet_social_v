import os
from pathlib import Path

# ✅ Base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# ✅ Security settings
SECRET_KEY = os.environ.get("SECRET_KEY", "your-default-secret-key")
DEBUG = os.environ.get("DEBUG", "False") == "True"
ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "siqnet.tech").split(",")

# ✅ Installed apps
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Third-party apps
    "rest_framework",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "corsheaders",

    # Custom apps
    "userauth",
    "userposts",
    "community",
    "accounts",
    "siqposts",
    "versnet",
]

# ✅ Middleware
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# ✅ CORS settings
CORS_ALLOW_ALL_ORIGINS = True

# ✅ URL and WSGI config
ROOT_URLCONF = "siqnet_social.urls"
WSGI_APPLICATION = "siqnet_social.wsgi.application"

# ✅ Templates
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# ✅ Database (PostgreSQL)
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("DB_NAME", "siqnet"),
        "USER": os.environ.get("DB_USER", "postgres"),
        "PASSWORD": os.environ.get("DB_PASSWORD", ""),
        "HOST": os.environ.get("DB_HOST", "localhost"),
        "PORT": os.environ.get("DB_PORT", "5432"),
    }
}

# ✅ Password validation
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# ✅ Internationalization
LANGUAGE_CODE = os.environ.get("LANGUAGE_CODE", "en-us")
TIME_ZONE = os.environ.get("TIME_ZONE", "Africa/Lusaka")
USE_I18N = True
USE_TZ = True

# ✅ Static files
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# ✅ Media files
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# ✅ Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# ✅ Authentication
AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)

SITE_ID = 1
LOGIN_REDIRECT_URL = "/userauth/profile/"

# ✅ Security headers for production
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# ✅ Logging
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "INFO",
    },
}
