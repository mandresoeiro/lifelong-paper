"""
LIFELONG PAPER
Base Settings

Este arquivo contém TODAS as configurações comuns
a qualquer ambiente (dev / prod / test).

NUNCA coloque DEBUG=True aqui.
NUNCA coloque secrets diretos aqui.
"""

from pathlib import Path

# ==================================================
# PATHS
# ==================================================

# Raiz do projeto
BASE_DIR = Path(__file__).resolve().parent.parent.parent


# ==================================================
# CORE SETTINGS
# ==================================================

SECRET_KEY = "dev-insecure-key-change-later"
# 🔴 PRODUÇÃO:
# SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

DEBUG = False  # DEV define isso no dev.py

ALLOWED_HOSTS = []


# ==================================================
# APPLICATIONS
# ==================================================


DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "visual",
    "accounts",
    "profiles",
    "papers",
    "devroadmap",
    "projetos",
    "cursos",
]

PROJECT_APPS = [
    # apps do Lifelong Paper entram aqui
    # 'papers',
    # 'checklist',
    # 'diary',
    # 'ideas',
]

THIRD_PARTY_APPS = [
    # futuras libs (ex: django_filters, rest_framework)
]

INSTALLED_APPS = DJANGO_APPS + PROJECT_APPS + THIRD_PARTY_APPS


# ==================================================
# MIDDLEWARE
# ==================================================

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    # 🔴 Produção:
    # 'whitenoise.middleware.WhiteNoiseMiddleware',
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


# ==================================================
# URLS / ASGI / WSGI
# ==================================================

ROOT_URLCONF = "core.urls"

WSGI_APPLICATION = "core.wsgi.application"
ASGI_APPLICATION = "core.asgi.application"


# ==================================================
# TEMPLATES
# ==================================================

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        # Templates globais
        "DIRS": [
            BASE_DIR / "templates",
        ],
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


# ==================================================
# DATABASE
# ==================================================

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# 🔴 PRODUÇÃO (exemplo PostgreSQL):
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': os.environ.get('DB_NAME'),
#         'USER': os.environ.get('DB_USER'),
#         'PASSWORD': os.environ.get('DB_PASSWORD'),
#         'HOST': os.environ.get('DB_HOST'),
#         'PORT': '5432',
#     }
# }


# ==================================================
# AUTH / PASSWORDS
# ==================================================

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": (
            "django.contrib.auth.password_validation"
            ".UserAttributeSimilarityValidator"
        )
    },
    {"NAME": ("django.contrib.auth.password_validation" ".MinimumLengthValidator")},
    {"NAME": ("django.contrib.auth.password_validation" ".CommonPasswordValidator")},
    {"NAME": ("django.contrib.auth.password_validation" ".NumericPasswordValidator")},
]


LOGIN_URL = "/admin/login/"
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"


# ==================================================
# INTERNATIONALIZATION
# ==================================================

LANGUAGE_CODE = "pt-br"
TIME_ZONE = "America/Belem"
USE_I18N = True
USE_TZ = True


# ==================================================
# STATIC & MEDIA
# ==================================================

STATIC_URL = "/static/"

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

# 🔴 PRODUÇÃO:
# STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"


# ==================================================
# SECURITY (DEFAULT SAFE)
# ==================================================

CSRF_COOKIE_HTTPONLY = True
SESSION_COOKIE_HTTPONLY = True

# 🔴 PRODUÇÃO:
# CSRF_COOKIE_SECURE = True
# SESSION_COOKIE_SECURE = True
# SECURE_SSL_REDIRECT = True
# SECURE_HSTS_SECONDS = 31536000
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True
# SECURE_HSTS_PRELOAD = True


# ==================================================
# LOGGING (BASE)
# ==================================================

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "simple": {
            "format": "[{levelname}] {message}",
            "style": "{",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "simple",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "INFO",
    },
}


# ==================================================
# DEFAULTS
# ==================================================

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
