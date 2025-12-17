from django.urls import path
from .views import CursoListView, CursoCreateView, CursoDetailView, CursoUpdateView, CursoDeleteView



urlpatterns = [
    path("", CursoListView.as_view(), name="list"),
    path("novo/", CursoCreateView.as_view(), name="create"),
    path("<int:pk>/", CursoDetailView.as_view(), name="detail"),
    path("<int:pk>/editar/", CursoUpdateView.as_view(), name="edit"),
    path("<int:pk>/excluir/", CursoDeleteView.as_view(), name="delete"),
]
