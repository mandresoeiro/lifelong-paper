from django.contrib import admin
from .models import Curso, Aula

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ("nome", "plataforma", "instrutor", "progresso", "criado_em")
    search_fields = ("nome", "plataforma", "instrutor")
    list_filter = ("plataforma",)

@admin.register(Aula)
class AulaAdmin(admin.ModelAdmin):
    list_display = ("titulo", "curso", "ordem", "assistido")
    search_fields = ("titulo",)
    list_filter = ("curso", "assistido")
