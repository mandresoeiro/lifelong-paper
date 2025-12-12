from django.urls import path
from .views import PaperListView, PaperCreateView

app_name = "papers"

urlpatterns = [
    path("", PaperListView.as_view(), name="list"),
    path("new/", PaperCreateView.as_view(), name="create"),
]
