from django.db import models
from django.conf import settings

class Curso(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nome = models.CharField(max_length=120)
    plataforma = models.CharField(max_length=60, blank=True, help_text="Ex: Udemy, Alura, YouTube")
    instrutor = models.CharField(max_length=80, blank=True)
    url = models.URLField(blank=True, help_text="Link do curso")
    imagem = models.ImageField(upload_to="cursos_capa/", blank=True, null=True, help_text="Capa do curso")
    descricao = models.TextField(blank=True)
    progresso = models.PositiveSmallIntegerField(default=0, help_text="Progresso do curso em % (0 a 100)")
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome

class Aula(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name="aulas")
    titulo = models.CharField(max_length=120)
    ordem = models.PositiveSmallIntegerField(default=1)
    duracao = models.CharField(max_length=20, blank=True, help_text="Ex: 10m, 1h20")
    assistido = models.BooleanField(default=False)
    url = models.URLField(blank=True, help_text="Link da aula")
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["ordem"]

    def __str__(self):
        return f"{self.ordem}. {self.titulo}"
