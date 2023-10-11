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
    path('fishs/<int:fish_id>/reviewdelete/<int:pk>/', views.FishReviewDeleteView.as_view(), name="review_delete"),
    path('fishs/<int:fish_id>/reviewedit/<int:pk>/', views.FishReviewUpdateView.as_view(), name="review_edit"),
]
