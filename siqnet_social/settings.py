import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# 🔧 Media Files Configuration
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# ✅ Static Files (already present, but shown for context)
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
