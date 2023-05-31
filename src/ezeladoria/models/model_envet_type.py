# flake8: noqa
from django.db import models


class TipoEvento(models.Model):
    Tipo_Evento_Id = models.AutoField(
        primary_key=True, verbose_name="Código Tipo")
    Descricao = models.CharField(
        max_length=50, help_text="Descrição", verbose_name="Descrição")
    Inativo = models.BooleanField(default=False, verbose_name="Inativo")

    def __init__(self, *args, **kwargs):
        self.queryset = TipoEvento.objects.filter(Inativo=False)
        super(TipoEvento, self).__init__(*args, **kwargs)

    def __str__(self) -> str:
        return self.Descricao

    class Meta:
        verbose_name = "Tipo de Evento"
        verbose_name_plural = "Tipos de Eventos"
