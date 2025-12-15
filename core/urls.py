from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("visual.urls")),
    path("papers/", include("papers.urls")),
    path("devroadmap/", include("devroadmap.urls")),
    path("projetos/", include("projetos.urls")),
    path("cursos/", include("cursos.urls", namespace="cursos")),
]
