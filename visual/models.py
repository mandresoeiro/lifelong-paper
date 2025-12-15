
from django.db import models
from django.conf import settings

class ChecklistItem(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	description = models.CharField(max_length=255)
	done = models.BooleanField(default=False)
	date = models.DateField(auto_now_add=True)

	def __str__(self):
		return f"{self.description} ({'feito' if self.done else 'pendente'})"


class LogDiario(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	date = models.DateField(auto_now_add=True)
	como_foi = models.TextField(blank=True)
	humor = models.CharField(max_length=50, blank=True)
	observacoes = models.TextField(blank=True)

	def __str__(self):
		return f"Log de {self.user.username} em {self.date}"


class Ideia(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	texto = models.TextField()
	data_criacao = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.texto[:40] + ("..." if len(self.texto) > 40 else "")
