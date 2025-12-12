import os
from django.core.wsgi import get_wsgi_application

# 🔧 Produção (futuro)
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings.prod')

# 🟢 Desenvolvimento
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings.dev")

application = get_wsgi_application()
