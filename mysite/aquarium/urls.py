from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('species/', views.species, name="species"),
    path('species/<int:specie_id>', views.species, name='specie'),
    path('fishs/', views.FishListView.as_view(), name='fishs'),
    path('search/', views.search, name='search'),
]
