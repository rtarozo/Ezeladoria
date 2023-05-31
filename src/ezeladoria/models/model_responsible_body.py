# flake8: noqa
from django.db import models

from .model_company import Empresa
from .model_envet_type import TipoEvento


class Orgao_Responsavel(models.Model):
    Acionaveis_Id = models.AutoField(
        primary_key=True, verbose_name="Sequencia")
    Descricao = models.CharField(
        max_length=50, help_text="Descrição", verbose_name="Descrição")
    Inativo = models.BooleanField(default=False, verbose_name="Inativo")
    Email_Principal = models.EmailField(
        max_length=100, help_text="Email do responsável", verbose_name="Email")
    Tipo_Evento = models.ForeignKey(TipoEvento, on_delete=models.CASCADE)
    Data_Cadastro = models.DateField(
        auto_now_add=True, verbose_name="Data de Cadastro")
    Empresa = models.OneToOneField(
        Empresa, on_delete=models.PROTECT, related_name="Orgao_Responsavel.Empresa+")

    def __init__(self, *args, **kwargs):
        self.queryset = Orgao_Responsavel.objects.filter(Inativo=False)
        super(Orgao_Responsavel, self).__init__(*args, **kwargs)

    def __str__(self) -> str:
        return self.Descricao

    class Meta:
        verbose_name = "Orgão Responsável"
        verbose_name_plural = "Orgãos Responsáveis"
