

from django.views.generic import TemplateView, ListView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import ChecklistItem, LogDiario, Ideia


class DashboardView(TemplateView):
    template_name = "visual/dashboard.html"


class ChecklistListView(LoginRequiredMixin, ListView):
    model = ChecklistItem
    template_name = "visual/checklist_list.html"
    context_object_name = "checklist"

    def get_queryset(self):
        return ChecklistItem.objects.filter(user=self.request.user).order_by('-id')


class ChecklistCreateView(LoginRequiredMixin, CreateView):
    model = ChecklistItem
    fields = ["description"]
    template_name = "visual/checklist_form.html"
    success_url = reverse_lazy("visual:checklist-list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class LogDiarioCreateView(LoginRequiredMixin, CreateView):
    model = LogDiario
    fields = ["como_foi", "humor", "observacoes"]
    template_name = "visual/logdiario_form.html"
    success_url = reverse_lazy("visual:dashboard")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class IdeiaListView(LoginRequiredMixin, ListView):
    model = Ideia
    template_name = "visual/ideia_list.html"
    context_object_name = "ideias"

    def get_queryset(self):
        return Ideia.objects.filter(user=self.request.user).order_by('-data_criacao')


class IdeiaCreateView(LoginRequiredMixin, CreateView):
    model = Ideia
    fields = ["texto"]
    template_name = "visual/ideia_form.html"
    success_url = reverse_lazy("visual:ideia-list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
