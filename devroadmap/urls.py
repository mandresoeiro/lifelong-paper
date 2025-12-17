from django.urls import path
from .views import RoadmapEntryListView, RoadmapEntryCreateView, RoadmapEntryDetailView, RoadmapEntryUpdateView, RoadmapEntryDeleteView



urlpatterns = [
    path("", RoadmapEntryListView.as_view(), name="list"),
    path("novo/", RoadmapEntryCreateView.as_view(), name="create"),
    path("<int:pk>/", RoadmapEntryDetailView.as_view(), name="detail"),
    path("<int:pk>/editar/", RoadmapEntryUpdateView.as_view(), name="edit"),
    path("<int:pk>/excluir/", RoadmapEntryDeleteView.as_view(), name="delete"),
]
