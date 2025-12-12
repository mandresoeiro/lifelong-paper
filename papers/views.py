from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import Paper


class PaperListView(ListView):
    model = Paper
    template_name = "papers/paper_list.html"
    context_object_name = "papers"


class PaperCreateView(CreateView):
    model = Paper
    fields = ["title", "content"]
    template_name = "papers/paper_form.html"
    success_url = reverse_lazy("papers:list")
