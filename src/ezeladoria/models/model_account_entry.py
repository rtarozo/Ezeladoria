# flake8: noqa
from django.db import models

from .model_account import ContaCorrente
from .model_default_historic import HistoricoPadrao


class LancamentoConta(models.Model):
    TIPO_CHOICES = (("D", "Débito"), ("C", "Crédito"))
    Lancamento_Id = models.AutoField(
        primary_key=True, verbose_name="Código Lançamento")
    Data_lancamento = models.DateField(
        "Data de Lançamento", auto_now_add=True, db_index=True)
    Tipo_Lacamento = models.CharField(
        max_length=1, choices=TIPO_CHOICES, blank=False, null=False)
    Saldo_Anterior = models.FloatField(
        null=False, blank=False, default=0.0, editable=True)
    Valor_Debito = models.FloatField(
        null=False, blank=False, default=0.0, editable=True)
    Valor_Credito = models.FloatField(
        null=False, blank=False, default=0.0, editable=True)
    Saldo_Atual = models.FloatField(
        null=False, blank=False, default=0.0, editable=True)
    ContaCorrente_Id = models.ForeignKey(
        ContaCorrente, on_delete=models.PROTECT, related_name="ContaCorrente")
    Historico_Id = models.ForeignKey(
        HistoricoPadrao, on_delete=models.PROTECT, related_name="Históricos")
    Historico_Lancamento = models.TextField(
        max_length=200, help_text="Histórico")

    def __str__(self):
        return f"Data {self.Data_lancamento}, Saldo Anterior R$ {self.Saldo_Anterior}, Crédito R$ {self.Valor_Credito}, Débito R$ {self.Valor_Debito}, Saldo Atual R$ {self.Saldo_Atual}"

    class Meta:
        verbose_name = "Lançamento em Conta"
        verbose_name_plural = "Lançamentos em Conta"
