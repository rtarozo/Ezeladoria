# flake8: noqa
from django.db import models

from .model_company import Empresa


class ContaCorrente(models.Model):
    TIPO_CHOICES = (
        ("11", "Física"),
        ("12", "Jurídica"),
        ("13", "Poupança"),
        ("14", "Aplicação"),
        ("15", "Juros"),
        ("16", "Multa"),
    )
    Conta_Corrente_Id = models.AutoField(
        primary_key=True, verbose_name="Código Conta")
    Tipo_Conta = models.CharField(
        max_length=2, choices=TIPO_CHOICES, blank=False, null=False)
    Codigo_Conta = models.IntegerField(verbose_name="Número Conta", default=0)
    Digito_Conta = models.IntegerField(verbose_name="Dv", default=0)
    Descricao = models.CharField(
        max_length=50, help_text="Descrição", verbose_name="Descrição")
    Data_Cadastro = models.DateField(
        verbose_name="Data de Cadastro", auto_now_add=True, db_index=True)
    Saldo = models.FloatField(null=True, blank=True, default=0.0)
    Data_Atualizacao = models.DateField(
        verbose_name="Data de Atualização", auto_now=True, db_index=True)
    Empresa = models.OneToOneField(
        Empresa, on_delete=models.PROTECT, related_name="Empresa")
    Limite_Credito = models.FloatField(
        null=True, blank=True, default=0.0, verbose_name="Limite de Crédito")

    def save(self, *args, **kwargs):
        if self.Tipo_Conta is None:
            self.Tipo_Conta = "12"
        if self.Codigo_Conta is None:
            self.Codigo_Conta = set(self.Tipo_Conta).union(
                str(self.Conta_Corrente_Id))
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.Descricao

    class Meta:
        verbose_name = "Conta Corrente"
        verbose_name_plural = "Contas Corrente"

    @classmethod
    def CriarConta(cls, object):
        numeroconta = str(object.ContaCorrente_Id)
        tipoconta = str(object.TipoConta)
        cls.Codigo_Conta = f"{tipoconta}{numeroconta:08}"
        return cls

    @classmethod
    def CalculaDigito(cls, object):
        # numeroconta = cls.Codigo_Conta

        # cls.Digito_Conta = int(numeroconta) % 11
        return cls


def CriaConta(sender, instance, created, **kwargs):
    if created:
        numero: int = 0

        paramObject = Parametro.objects.get(Codigo="SEQ_CONTA")

        # numero = val(paramObject.Valor) += 1

        # Parametro.objects.save()

        ContaCorrente.objects.create(
            Empresa=instance,
            Limite_Credito=1000,
            Tipo_Conta="12",
            Codigo_Conta=f"12{numero}",
        )
        return instance
