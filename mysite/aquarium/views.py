from django.shortcuts import render
from django.views import generic
from .models import Species


# Create your views here.


class SpeciesListView(generic.ListView):
    model = Species
    template_name = "species.html"
    context_object_name = 'species'
