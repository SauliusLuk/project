from django.shortcuts import render
from .models import Projektas, Darbuotojas, Darbas
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
def index(request):
    visi_projektai = Projektas.objects.all().count()
    visi_darbuotojai = Darbuotojas.objects.all().count()

    context = {
            'visi_projektai': visi_projektai,
            'visi_darbuotojai': visi_darbuotojai,
        }

    return render(request, 'index.html', context=context)

def darbai(request):
    context = {'Darbai': Darbas.objects.all(), }
    return render(request, 'darbai.html', context=context)

def darbas(request):
    context = {'Darbas': Darbas.objects.all(), }
    return render(request, 'darbas.html', context=context)

class ProjektasListView(generic.ListView):
    model = Projektas
    template_name = 'projektai.html'
    context_object_name = 'projektai'
    paginate_by = 3

class ManoProjektaiListView(generic.ListView, LoginRequiredMixin):
    model = Projektas
    template_name = 'project/manoprojektai.html'
    paginate_by = 3

    def get_queryset(self):
        return Projektas.objects.filter(vadovas=self.request.user)

class ManoProjektasDetailView(generic.DetailView):
    model = Projektas