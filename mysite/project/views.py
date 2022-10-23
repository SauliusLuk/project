from django.shortcuts import render
from .models import Projektas, Darbuotojas, Darbas
from django.views import generic
def index(request):
    visi_projektai = list(Projektas.objects.all().values_list('pavadinimas',))
    visi_darbuotojai = Darbuotojas.objects.all().count()

    context = {
            'visi_projektai': visi_projektai,
            'visi_darbuotojai': visi_darbuotojai,
        }

    return render(request, 'index.html', context=context)

def darbai(request):
    context = {'Darbai': Darbas.objects.all(), }
    return render(request, 'darbai.html', context=context)

class ProjektasListView(generic.ListView):
    model = Projektas
    template_name = 'projektai.html'
    context_object_name = 'projektai'
    paginate_by = 5