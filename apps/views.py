from django.shortcuts import render
from django.views.generic import CreateView

from apps.forms import RegisterModelForm
from apps.models import Planet, Galaxy, Group, Gallery, Exploration, About, Holes_Matter, Register


def index_view(request):
    context = {
        'planets': Planet.objects.all(),
        'galaxies': Galaxy.objects.all(),
        'groups': Group.objects.all(),
        'galleries': Gallery.objects.all(),
        'Explorations': Exploration.objects.all(),
        'Abouts': About.objects.all(),
        'holes_matters': Holes_Matter.objects.all(),
        'registers': Register.objects.all(),
        'interests': Register.Interests.choices

    }
    return render(request, 'index.html', context)


class RegisterCreateView(CreateView):
    model = Register
    form_class = RegisterModelForm
    success_url = '/'




# CRUD - Create, Read, Update, Delete

