from django.urls import path
from .views import (
    DashboardView,
    ChecklistListView, ChecklistCreateView,
    LogDiarioCreateView,
    IdeiaListView, IdeiaCreateView,
)

app_name = "visual"

urlpatterns = [
    path("", DashboardView.as_view(), name="dashboard"),
    path("checklist/", ChecklistListView.as_view(), name="checklist-list"),
    path("checklist/novo/", ChecklistCreateView.as_view(), name="checklist-create"),
    path("log/novo/", LogDiarioCreateView.as_view(), name="logdiario-create"),
    path("ideias/", IdeiaListView.as_view(), name="ideia-list"),
    path("ideias/nova/", IdeiaCreateView.as_view(), name="ideia-create"),
]
