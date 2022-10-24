from django.contrib import admin
from .models import Projektas, Klientas, Darbuotojas, Darbas, Saskaita


# Register your models here.

class ProjektasInLine(admin.TabularInline):
    model = Saskaita
    extra = 0
    can_delete = False

class ProjektasAdmin(admin.ModelAdmin):
    inlines = [ProjektasInLine]

class ProjektasDetail(admin.ModelAdmin):
    list_display = ('pavadinimas', 'klientas', 'vadovas', 'display_darbuotojai', 'saskaitos')
    list_filter = ('pavadinimas', 'klientas', 'vadovas', 'saskaitos')

class ProjektasID(admin.ModelAdmin):
    readonly_fields = ('id',)

class KlientasDetail(admin.ModelAdmin):
    list_display = ('vardas', 'pavarde', 'imone')
    search_fields = ('vardas', 'pavarde', 'imone')

class SaskaitaDetail(admin.ModelAdmin):
    list_display = ('pradzia', 'suma')


class DarbasDetail(admin.ModelAdmin):
    list_display = ('pavadinimas', 'pastabos')


admin.site.register(Projektas, ProjektasAdmin,)
admin.site.register(Klientas, KlientasDetail)
admin.site.register(Darbuotojas)
admin.site.register(Darbas, DarbasDetail)
admin.site.register(Saskaita, SaskaitaDetail)
