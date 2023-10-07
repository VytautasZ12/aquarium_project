from django.shortcuts import render
from django.views import generic
from .models import Specie, Fish


# Create your views here.


class SpecieListView(generic.ListView):
    model = Specie
    template_name = "specie.html"
    context_object_name = 'specie'


class FishListView(generic.ListView):
    model = Fish
    template_name = "fish.html"
    context_object_name = 'fish'