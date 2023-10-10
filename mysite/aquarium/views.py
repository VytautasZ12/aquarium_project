from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse
from django.views import generic
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from .models import Specie, Fish
from django.db.models import Q
from django.shortcuts import redirect


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
    context_object_name = "fishs"
    paginate_by = 6


class FishDetailView(generic.DetailView):
    model = Fish
    template_name = "fish.html"
    context_object_name = "fish"


class SpecieListView(generic.ListView):
    model = Specie
    template_name = "species.html"
    context_object_name = "species"


def specie(request, specie_id):
    specie = get_object_or_404(Specie, pk=specie_id)
    context = {
        'specie': specie,
    }
    return render(request, 'specie.html', context=context)


def search(request):
    query = request.GET.get('query')
    search_results = Fish.objects.filter(
        Q(fish_title__icontains=query) | Q(origin__icontains=query) | Q(species__specie_name__icontains=query))
    return render(request, 'search.html', {'fishs': search_results, 'query': query})


@csrf_protect
def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, ("Username %s already exists!") % username)
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, ("Email %s already exists!") % email)
                    return redirect('register')
                else:
                    User.objects.create_user(username=username, email=email, password=password)
                    messages.info(request, ("User %s registered!") % username)
                    return redirect('login')
        else:
            messages.error(request, ('Passwords do not match!'))
            return redirect('register')
    else:
        return render(request, 'registration/register.html')
