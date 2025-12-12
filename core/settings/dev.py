from .base import *

DEBUG = True

ALLOWED_HOSTS = []

# Segurança relaxada para desenvolvimento
CSRF_COOKIE_SECURE = False
SESSION_COOKIE_SECURE = False
SECURE_SSL_REDIRECT = False
