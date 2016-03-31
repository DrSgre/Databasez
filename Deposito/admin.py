from django.contrib import admin
import Deposito
import django.http as http
from .models import Campione
import datetime

@admin.register(Campione)
class ListaCampioni(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('data', 'nome', 'valore', 'valore2', 'valore3', 'BAR')
        }),
    )
    list_display = ('data', 'nome', 'valore','valore2', 'valore3', 'BAR')
    search_fields = ['data', 'nome', 'valore', 'valore2', 'valore3', 'BAR']

    k = 0

def insert(dataz, nomez, valorez, valorez2, valorez3, k):
    k = ListaCampioni.k
    if (Campione.objects.filter(codice = k).count() == 0):
        v = Campione(data = dataz, nome = nomez, valore = valorez, valore2 = valorez2, valore3 = valorez3, BAR = "#" + str(k), codice = k)
        v.save()
        ListaCampioni.k = ListaCampioni.k + 1
    else:
        ""

in_file = open("Deposito/Dati.txt", "r")

while (in_file.readline() != ""):
    a = in_file.readline()
    b = in_file.readline()
    c = in_file.readline()
    d = in_file.readline()
    e = in_file.readline()
    l = in_file.readline()

    insert(a, b, c, d, e, l)
