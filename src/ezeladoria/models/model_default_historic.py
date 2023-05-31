# flake8: noqa
from django.db import models


class HistoricoPadrao(models.Model):
    Historico_Id = models.AutoField(
        primary_key=True, verbose_name="Código Histórico")
    Descricao = models.CharField(max_length=50, help_text="Descrição")
    Historico = models.TextField(max_length=200, help_text="Histórico")
    Inativo = models.BooleanField(default=False)

    def __init__(self, *args, **kwargs):
        self.queryset = HistoricoPadrao.objects.filter(Inativo=False)
        super(HistoricoPadrao, self).__init__(*args, **kwargs)

    def __str__(self) -> str:
        return self.Descricao

    class Meta:
        verbose_name = "Histórico Padrão"
        verbose_name_plural = "Históricos Padrões"
