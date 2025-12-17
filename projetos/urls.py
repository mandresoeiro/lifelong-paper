from django.urls import path
from .views import ProjetoListView, ProjetoCreateView, ProjetoDetailView, ProjetoUpdateView, ProjetoDeleteView, ProjetoComentarioCreateView



urlpatterns = [
    path("", ProjetoListView.as_view(), name="list"),
    path("novo/", ProjetoCreateView.as_view(), name="create"),
    path("<int:pk>/", ProjetoDetailView.as_view(), name="detail"),
    path("<int:pk>/editar/", ProjetoUpdateView.as_view(), name="edit"),
    path("<int:pk>/excluir/", ProjetoDeleteView.as_view(), name="delete"),
    path("<int:pk>/anotacao/", ProjetoComentarioCreateView.as_view(), name="anotacao"),
]
