from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Curso, Aula
from .forms import CursoForm, AulaForm
from django.shortcuts import get_object_or_404, redirect

class CursoListView(LoginRequiredMixin, ListView):
    model = Curso
    template_name = "cursos/curso_list.html"
    context_object_name = "cursos"

    def get_queryset(self):
        return Curso.objects.filter(user=self.request.user).order_by("-criado_em")

class CursoCreateView(LoginRequiredMixin, CreateView):
    model = Curso
    form_class = CursoForm
    template_name = "cursos/curso_form.html"
    success_url = reverse_lazy("cursos:list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class CursoDetailView(LoginRequiredMixin, DetailView):
    model = Curso
    template_name = "cursos/curso_detail.html"
    context_object_name = "curso"

class CursoUpdateView(LoginRequiredMixin, UpdateView):
    model = Curso
    form_class = CursoForm
    template_name = "cursos/curso_form.html"
    success_url = reverse_lazy("cursos:list")

class CursoDeleteView(LoginRequiredMixin, DeleteView):
    model = Curso
    template_name = "cursos/curso_confirm_delete.html"
    success_url = reverse_lazy("cursos:list")

# Aula CRUD pode ser expandido depois
