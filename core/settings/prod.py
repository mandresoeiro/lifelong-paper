from .base import *

DEBUG = False

ALLOWED_HOSTS = [
    "seudominio.com",
]

# 🔒 Segurança para produção
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True

# STATIC_ROOT = BASE_DIR / 'staticfiles'
