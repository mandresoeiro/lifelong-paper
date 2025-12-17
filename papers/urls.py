from django.urls import path
from .views import PaperListView, PaperCreateView



urlpatterns = [
    path("", PaperListView.as_view(), name="list"),
    path("new/", PaperCreateView.as_view(), name="create"),
]
