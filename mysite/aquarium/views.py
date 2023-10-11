from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse
from django.views import generic
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from django.views.generic.edit import FormMixin
from .froms import FishReviewForm, UserUpdateForm, ProfilisUpdateForm
from .models import Specie, Fish, FishReview
from django.db.models import Q
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


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


class FishDetailView(FormMixin, generic.DetailView):
    model = Fish
    template_name = "fish.html"
    context_object_name = "fish"
    form_class = FishReviewForm

    def get_success_url(self):
        return reverse('fish', kwargs={"pk": self.object.id})

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.instance.fish = self.object
        form.instance.reviewer = self.request.user
        form.save()
        return super().form_valid(form)


class SpecieListView(generic.ListView):
    model = Specie
    template_name = "species.html"
    context_object_name = "species"


class FishReviewDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = FishReview
    template_name = "review_delete.html"
    context_object_name = 'review'

    def get_success_url(self):
        return reverse('fish', kwargs={"pk": self.kwargs['fish_id']})

    def test_func(self):
        return self.get_object().reviewer == self.request.user


class FishReviewUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = FishReview
    template_name = "review_edit.html"
    context_object_name = 'review'
    fields = ['content']

    def get_success_url(self):
        return reverse('fish', kwargs={"pk": self.kwargs['fish_id']})

    def test_func(self):
        return self.get_object().reviewer == self.request.user

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.post = Fish.objects.get(pk=self.kwargs['fish_id'])
        form.save()
        return super().form_valid(form)


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


@login_required
def profilis(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfilisUpdateForm(request.POST, request.FILES, instance=request.user.profilis)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, "Profilis atnaujintas")
            return redirect('profilis')

    u_form = UserUpdateForm(instance=request.user)
    p_form = ProfilisUpdateForm(instance=request.user.profilis)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, "profilis.html", context=context)
