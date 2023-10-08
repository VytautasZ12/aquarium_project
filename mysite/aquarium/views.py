from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse
from django.views import generic
from .models import Specie, Fish
from django.core.paginator import Paginator
from django.db.models import Q


# Create your views here.


def index(request):
    num_species = Specie.objects.count()
    num_fishs = Fish.objects.count()

    context = {
        'num_species': num_species,
        'num_fish': num_fishs,
    }
    return render(request, 'index.html', context=context)


class FishListView(generic.ListView):
    model = Fish
    template_name = "fishs.html"
    context_object_name = "fihs"
    paginate_by = 6


def species(request):
    paginator = Paginator(Specie.objects.all(), 2)
    page_number = request.GET.get('page')
    paged_species = paginator.get_page(page_number)
    context = {
        'authors': paged_species
    }
    return render(request, 'species.html', context=context)


def specie(request, specie_id):
    specie = get_object_or_404(Specie, pk=specie_id)
    context = {
        'specie': specie,
    }
    return render(request, 'specie.html', context=context)


def search(request):
    query = request.GET.get('query')
    search_results = Fish.objects.filter(
        Q(title__icontains=query) | Q(summary__icontains=query) | Q(species__specie_name__icontains=query))
    return render(request, 'search.html', {'fishs': search_results, 'query': query})
