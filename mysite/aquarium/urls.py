from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('species/', views.SpecieListView.as_view(), name="species"),
    path('species/<int:specie_id>', views.specie, name='specie'),
    path('fishs/', views.FishListView.as_view(), name='fishs'),
    path('fishs/<int:pk>', views.FishDetailView.as_view(), name='fish'),
    path('search/', views.search, name='search'),
    path('register/', views.register, name="register"),
    path('profilis/', views.profilis, name='profilis'),
    path('usercomments/', views.FishDetailView.as_view(), name='usercomments'),
]
