from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.

class Projektas(models.Model):
    pavadinimas = models.CharField('Projekto pavadinimas', max_length=200, help_text='Projekto pavadinimas')
    pradzia = models.DateTimeField('Pradžios data', max_length=200, help_text='Įveskite projekto pradžios datą')
    pabaiga = models.DateTimeField('Pabaigos data', max_length=200, help_text='Įveskite projekto pabaigos datą')
    klientas = models.CharField('Klientas', max_length=200, help_text='Įveskite projekto užsakovą')
    vadovas = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    darbuotojai = models.ManyToManyField('Darbuotojas', max_length=200, help_text='Įveskite darbuotojo vardą ir pavardę')
    darbai = models.ForeignKey('Darbas', on_delete=models.SET_NULL, null=True, blank=True, max_length=200)
    saskaitos = models.ForeignKey('Saskaita', on_delete=models.SET_NULL, null=True, blank=True, help_text='Įveskite sąskaitos numerį')
    nuotrauka = models.ImageField(default="default.png", upload_to="covers", null=True)

    def __str__(self):
        return f"{self.pavadinimas} - {self.klientas}"

    def display_darbuotojai(self):
        darbuotojai = self.darbuotojai.all()
        darbuotojai_names = list(darbuotojas.vardas for darbuotojas in darbuotojai)
        darbuotojai_str = ', '.join(darbuotojai_names)
        return darbuotojai_str

    display_darbuotojai.short_description = "Darbuotojai"

    class Meta:
        verbose_name = 'Projektas'
        verbose_name_plural = '1 - Projektai'
        ordering = ['id']


class Klientas(models.Model):
    vardas = models.CharField('Vardas', max_length=100)
    pavarde = models.CharField('Pavardė', max_length=100)
    imone = models.CharField('Įmonė', max_length=100)
    kontaktai = models.CharField('Kontaktai', max_length=200, help_text='Įveskite telefoną')

    def __str__(self):
        return f"{self.vardas} {self.pavarde} ({self.imone})"

    class Meta:
        verbose_name = 'Klientas'
        verbose_name_plural = '2 - Klientai'
        ordering = ['id']


class Darbuotojas(models.Model):
    vardas = models.CharField('Vardas', max_length=100, help_text='Įveskite darbuotojo vardą')
    pavarde = models.CharField('Pavardė', max_length=100, help_text='Įveskite darbuotojo pavardę')

    def __str__(self):
        return f"{self.vardas} {self.pavarde}"

    class Meta:
        verbose_name = 'Darbuotojas'
        verbose_name_plural = '3 - Darbuotojai'


class Darbas(models.Model):
    atsakingas_darbuotojas = models.ForeignKey('Darbuotojas', on_delete=models.SET_NULL, null=True, blank=True, max_length=200)
    pavadinimas = models.CharField('Pavadinimas', max_length=200, help_text='Įveskite darbo pavadinimą')
    pastabos = models.TextField ('Pastabos')

    def __str__(self):
        return self.pavadinimas

    class Meta:
        verbose_name = 'Darbas'
        verbose_name_plural = '4 - Darbai'
        ordering = ['id']


class Saskaita(models.Model):
    pavadinimas = models.ForeignKey('Projektas', on_delete=models.SET_NULL, null=True, blank=True, max_length=200)
    pradzia = models.DateTimeField('Išrašymo data', help_text='Įveskite sąskaitos išrašymo datą')
    suma = models.IntegerField('Suma')

    def __str__(self):
        return f"{self.pradzia} - {self.suma} EUR"

    class Meta:
        verbose_name = 'Sąskaita'
        verbose_name_plural = '5 - Sąskaitos'
