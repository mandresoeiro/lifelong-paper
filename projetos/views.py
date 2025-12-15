from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Projeto, ProjetoComentario

class ProjetoListView(LoginRequiredMixin, ListView):
    model = Projeto
    template_name = "projetos/projeto_list.html"
    context_object_name = "projetos"

    def get_queryset(self):
        qs = Projeto.objects.filter(user=self.request.user).order_by("-criado_em")
        q = self.request.GET.get("q")
        status = self.request.GET.get("status")
        tecnologia = self.request.GET.get("tecnologia")
        if q:
            qs = qs.filter(
                models.Q(nome__icontains=q) |
                models.Q(descricao__icontains=q) |
                models.Q(tecnologias__icontains=q)
            )
        if status:
            qs = qs.filter(status__icontains=status)
        if tecnologia:
            qs = qs.filter(tecnologias__icontains=tecnologia)
        return qs



class ProjetoCreateView(LoginRequiredMixin, CreateView):
    model = Projeto
    fields = ["nome", "descricao", "tecnologias", "status", "link", "repo", "demo", "docs", "data_inicio", "data_fim", "anotacoes", "imagem", "progresso"]
    template_name = "projetos/projeto_form.html"
    success_url = reverse_lazy("projetos:list")

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        form.enctype = 'multipart/form-data'
        return form

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ProjetoDetailView(LoginRequiredMixin, DetailView):
    model = Projeto
    template_name = "projetos/projeto_detail.html"
    context_object_name = "projeto"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comentarios"] = self.object.comentarios.select_related("user").all()
        return context


# View para adicionar comentário/anotação rápida
from django.views.generic.edit import FormView
from django.shortcuts import redirect, get_object_or_404
from django import forms

class ProjetoComentarioForm(forms.ModelForm):
    class Meta:
        model = ProjetoComentario
        fields = ["texto"]
        widgets = {
            "texto": forms.Textarea(attrs={"rows":2, "placeholder": "Escreva uma anotação rápida...", "class": "w-full border rounded px-3 py-2"}),
        }

class ProjetoComentarioCreateView(LoginRequiredMixin, FormView):
    form_class = ProjetoComentarioForm
    template_name = "projetos/comentario_form.html"

    def form_valid(self, form):
        projeto = get_object_or_404(Projeto, pk=self.kwargs["pk"], user=self.request.user)
        comentario = form.save(commit=False)
        comentario.projeto = projeto
        comentario.user = self.request.user
        comentario.save()
        return redirect("projetos:detail", pk=projeto.pk)



class ProjetoUpdateView(LoginRequiredMixin, UpdateView):
    model = Projeto
    fields = ["nome", "descricao", "tecnologias", "status", "link", "repo", "demo", "docs", "data_inicio", "data_fim", "anotacoes", "imagem", "progresso"]
    template_name = "projetos/projeto_form.html"
    success_url = reverse_lazy("projetos:list")

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        form.enctype = 'multipart/form-data'
        return form

    def get_queryset(self):
        return Projeto.objects.filter(user=self.request.user)

class ProjetoDeleteView(LoginRequiredMixin, DeleteView):
    model = Projeto
    template_name = "projetos/projeto_confirm_delete.html"
    success_url = reverse_lazy("projetos:list")

    def get_queryset(self):
        return Projeto.objects.filter(user=self.request.user)
