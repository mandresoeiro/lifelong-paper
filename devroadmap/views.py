
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import RoadmapEntry


class RoadmapEntryUpdateView(LoginRequiredMixin, UpdateView):
    model = RoadmapEntry
    fields = ["title", "tipo", "language", "code", "description", "tags", "is_favorite", "reused"]
    template_name = "devroadmap/roadmapentry_form.html"
    success_url = reverse_lazy("devroadmap:list")

    def get_queryset(self):
        return RoadmapEntry.objects.filter(user=self.request.user)


class RoadmapEntryDeleteView(LoginRequiredMixin, DeleteView):
    model = RoadmapEntry
    template_name = "devroadmap/roadmapentry_confirm_delete.html"
    success_url = reverse_lazy("devroadmap:list")

    def get_queryset(self):
        return RoadmapEntry.objects.filter(user=self.request.user)

class RoadmapEntryListView(LoginRequiredMixin, ListView):
    model = RoadmapEntry
    template_name = "devroadmap/roadmapentry_list.html"
    context_object_name = "entries"

    def get_queryset(self):
        qs = RoadmapEntry.objects.filter(user=self.request.user).order_by("-created_at")
        q = self.request.GET.get("q")
        if q:
            qs = qs.filter(title__icontains=q) | qs.filter(tags__icontains=q) | qs.filter(description__icontains=q)
        tipo = self.request.GET.get("tipo")
        if tipo:
            qs = qs.filter(tipo=tipo)
        return qs

class RoadmapEntryCreateView(LoginRequiredMixin, CreateView):
    model = RoadmapEntry
    fields = ["title", "tipo", "language", "code", "description", "tags", "is_favorite", "reused"]
    template_name = "devroadmap/roadmapentry_form.html"
    success_url = reverse_lazy("devroadmap:list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class RoadmapEntryDetailView(LoginRequiredMixin, DetailView):
    model = RoadmapEntry
    template_name = "devroadmap/roadmapentry_detail.html"
    context_object_name = "entry"
