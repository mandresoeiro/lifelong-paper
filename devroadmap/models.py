from django.db import models
from django.conf import settings

class RoadmapEntry(models.Model):
    TIPO_CHOICES = [
        ("codigo", "Código"),
        ("dica", "Dica"),
        ("script", "Script"),
        ("referencia", "Referência"),
        ("outro", "Outro"),
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES, default="codigo")
    code = models.TextField(blank=True)
    language = models.CharField(max_length=30, blank=True, help_text="Ex: python, bash, js")
    description = models.TextField(blank=True)
    tags = models.CharField(max_length=120, blank=True, help_text="Separe por vírgula")
    is_favorite = models.BooleanField(default=False)
    reused = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
