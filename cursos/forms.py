from django import forms
from .models import Curso, Aula

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ["nome", "plataforma", "instrutor", "url", "imagem", "descricao", "progresso"]
        widgets = {
            "descricao": forms.Textarea(attrs={"rows": 3, "class": "w-full border rounded px-3 py-2"}),
            "progresso": forms.NumberInput(attrs={"min": 0, "max": 100, "class": "w-full"}),
        }

class AulaForm(forms.ModelForm):
    class Meta:
        model = Aula
        fields = ["titulo", "ordem", "duracao", "assistido", "url"]
        widgets = {
            "titulo": forms.TextInput(attrs={"class": "w-full border rounded px-3 py-2"}),
            "duracao": forms.TextInput(attrs={"class": "w-full border rounded px-3 py-2"}),
            "url": forms.URLInput(attrs={"class": "w-full border rounded px-3 py-2"}),
        }
