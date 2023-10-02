from django.urls import path
from .views import SpeciesListView

urlpatterns = [
    path('', SpeciesListView.as_view(), name="Fish species"),
]
