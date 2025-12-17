# ---------------------------------------------
# 🧭 Projeto: LIFELONG-PAPER (SoeiroTech Clean Golden™)
# 📁 Arquivo: core/urls.py
# ---------------------------------------------
# Este arquivo centraliza todas as rotas do sistema:
# - Painel administrativo (admin/)
# - Endpoints de API (api/)
# - Apps internos (papers, projetos, etc.)
# - Fallback do React (index_view)
# ---------------------------------------------

from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from .views import index_view  # View que serve o React buildado
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


# ---------------------------------------------
# 🔹 1. Endpoint de Status / Health Check
# ---------------------------------------------
# Usado para verificar se o backend está no ar.
# Retorna "API OK ✅" quando acessado em /api/status/
def api_root(request):
    return HttpResponse("API OK ✅")


# ---------------------------------------------
# 🔹 2. URL Patterns (catálogo principal)
# ---------------------------------------------
urlpatterns = [

    # -----------------------------------------
    # 🔸 Seção 1 — Administração Django
    # -----------------------------------------
    path("admin/", admin.site.urls),  # Painel administrativo padrão

    # -----------------------------------------
    # 🔸 Seção 2 — Health Check (status da API)
    # -----------------------------------------
    path("api/status/", api_root),  # Teste rápido de conexão com backend

    # -----------------------------------------
    # 🔸 Seção 3 — APIs (REST Framework)
    # -----------------------------------------
    # Todos os módulos de API (tarefas, projetos, etc.)
    path("api/", include("tasks.urls")),        # API de Tarefas
    path("api/", include("projetos.urls")),     # API de Projetos
    path("api/", include("papers.urls")),       # API de Papers (caso tenha endpoints DRF)
    path("api/", include("devroadmap.urls")),   # API de Roadmap Dev
    path("api/", include("cursos.urls")),       # API de Cursos

    # -----------------------------------------
    # 🔸 Seção 4 — Aplicações Web Django (interface)
    # -----------------------------------------
    path("", include("visual.urls")),  # Interface principal do painel
    path("projetos/", include("projetos.urls")),  # Páginas de projetos
    path("papers/", include("papers.urls")),      # Páginas de papers
    path("devroadmap/", include("devroadmap.urls")),  # Roadmap do desenvolvedor
    path("cursos/", include("cursos.urls")),  # Cursos


    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),

    # -----------------------------------------
    # 🔸 Seção 5 — Fallback (Frontend React buildado)
    # -----------------------------------------
    # Se nenhuma rota acima for encontrada, o Django entrega o index.html do React.
    path("", index_view, name="index"),
]
