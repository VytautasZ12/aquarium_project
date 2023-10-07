from django.urls import path
from .views import SpecieListView, FishListView

urlpatterns = [
    path('', SpecieListView.as_view(), name="specie"),
    path('specie/<int:_pk>/', FishListView.as_view(), name='fish'),
]
