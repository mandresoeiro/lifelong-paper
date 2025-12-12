import os
from django.core.asgi import get_asgi_application

# 🔧 Produção (futuro)
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings.prod')

# 🟢 Desenvolvimento
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings.dev")

application = get_asgi_application()
