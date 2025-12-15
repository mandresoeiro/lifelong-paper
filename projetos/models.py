
from django.db import models
from django.conf import settings

# Modelo para comentários/anotações rápidas por projeto
class ProjetoComentario(models.Model):
    projeto = models.ForeignKey('Projeto', on_delete=models.CASCADE, related_name="comentarios")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    texto = models.TextField("Comentário/Anotação", max_length=1000)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-criado_em"]

    def __str__(self):
        return f"Comentário de {self.user} em {self.projeto.nome}"

class Projeto(models.Model):
    TECNOLOGIAS = [
        ("django", "Django"),
        ("drf", "Django REST"),
        ("react", "React"),
        ("python", "Python"),
        ("outro", "Outro"),
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nome = models.CharField(max_length=120)
    descricao = models.TextField(blank=True)
    tecnologias = models.CharField(max_length=120, blank=True, help_text="Separe por vírgula")
    status = models.CharField(max_length=40, blank=True, help_text="Ex: Em andamento, Concluído")
    link = models.URLField(blank=True, help_text="Link principal do projeto (ex: site)")
    repo = models.URLField(blank=True, help_text="Link do repositório (ex: GitHub)")
    demo = models.URLField(blank=True, help_text="Link de demonstração (ex: vídeo, deploy)")
    docs = models.URLField(blank=True, help_text="Link da documentação")
    data_inicio = models.DateField(null=True, blank=True)
    data_fim = models.DateField(null=True, blank=True)
    anotacoes = models.TextField(blank=True)
    imagem = models.ImageField(upload_to="projetos_capa/", blank=True, null=True, help_text="Capa ou logo do projeto")
    progresso = models.PositiveSmallIntegerField(default=0, help_text="Progresso do projeto em % (0 a 100)")
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome
