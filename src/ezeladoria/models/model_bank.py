# flake8: noqa
from django.db import models


class Banco(models.Model):
    Banco_Id = models.AutoField(primary_key=True, verbose_name="Sequencia")
    Banco_Codigo = models.CharField(max_length=4, help_text="Código")
    Descricao = models.CharField(max_length=50, help_text="Descrição")
    Inativo = models.BooleanField(default=False)

    def __init__(self, *args, **kwargs):
        self.queryset = Banco.objects.filter(Inativo=False)
        super(Banco, self).__init__(*args, **kwargs)

    def __str__(self) -> str:
        return self.Descricao

    class Meta:
        verbose_name = "Banco"
        verbose_name_plural = "Bancos"
