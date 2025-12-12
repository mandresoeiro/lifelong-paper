from django.contrib import admin
from .models import Paper


@admin.register(Paper)
class PaperAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "created_at", "updated_at")
    search_fields = ("title", "content")
    list_filter = ("created_at",)
