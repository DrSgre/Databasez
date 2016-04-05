from django.db import models
from django.utils import timezone

class Campione(models.Model):
    data = models.CharField(max_length = 10, verbose_name="Data e Ora")
    nome = models.CharField(max_length = 10)
    valore = models.CharField(max_length = 10, verbose_name = "Tensione")
    valore2 = models.CharField(max_length = 10, verbose_name = "Corrente")
    valore3 = models.CharField(max_length = 10, verbose_name = "Potenza")
    codice = models.CharField(max_length = 10, verbose_name = "Codice", editable = False)
    BAR = models.CharField(max_length = 10)
