# flake8: noqa
from django.db import models


class Parametro(models.Model):
    Parametro_Id = models.AutoField(
        primary_key=True, verbose_name="Sequencia Parametro")
    Descricao = models.CharField(max_length=50, help_text="Descrição")
    Codigo = models.CharField(max_length=50, help_text="Código")
    Valor = models.TextField(max_length=200, help_text="Valor")

    def __str__(self) -> str:
        return self.Codigo

    class Meta:
        verbose_name = "Parametro"
        verbose_name_plural = "Parametros"
