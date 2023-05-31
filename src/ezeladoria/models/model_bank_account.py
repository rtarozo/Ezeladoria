# flake8: noqa
from django.db import models

from .model_bank import Banco


class ContaBanco(models.Model):
    Conta_Corrente_Id = models.AutoField(
        primary_key=True, verbose_name="Sequencia")
    Codigo_Conta = models.IntegerField(
        verbose_name="Número Conta", default=0, unique=True)
    Banco = models.ForeignKey(
        Banco, on_delete=models.PROTECT, related_name="Banco")
    Digito_Conta = models.IntegerField(verbose_name="Dv", default=0)
    Agencia = models.CharField(
        max_length=6, help_text="Agência e DV", verbose_name="Agência e DV", default=0)
    Descricao = models.CharField(
        max_length=50, help_text="Descrição", verbose_name="Descrição")
    Data_Cadastro = models.DateField(
        auto_now_add=True, db_index=True, verbose_name="Data de Cadastro")
    Saldo = models.FloatField(null=True, blank=True, default=0.0)
    Data_Atualizacao = models.DateField(
        auto_now=True, db_index=True, verbose_name="Data de Atualização")
    Limite_Credito = models.FloatField(
        null=True, blank=True, default=0.0, verbose_name="Limite de Crédito")
    Inativo = models.BooleanField(default=False)

    def __init__(self, *args, **kwargs):
        self.queryset = ContaBanco.objects.filter(Inativo=False)
        super(ContaBanco, self).__init__(*args, **kwargs)

    def __str__(self) -> str:
        return self.Descricao

    class Meta:
        verbose_name = "Conta"
        verbose_name_plural = "Contas"
