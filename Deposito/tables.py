import django_tables2 as tables
from Deposito.models import Campione

class CampioneTable(tables.Table):
    datas = tables.Column(verbose_name="Data e Ora")
    names = tables.Column(verbose_name="Sensori")
    values = tables.Column(verbose_name="Valori")

    class Meta:
        attrs = {"class": "paleblue"}
