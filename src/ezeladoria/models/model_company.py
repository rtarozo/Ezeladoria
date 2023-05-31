# flake8: noqa

from django.contrib.auth.models import User
from django.db import models
from localflavor.br.models import BRCNPJField

from .model_adress import Endereco


class Empresa(models.Model):
    Empresa_Id = models.AutoField(
        primary_key=True, verbose_name="Código Empresa")
    Razao_Social = models.CharField(
        max_length=100, help_text="Razão Social da empresa")
    Nome_Fantasia = models.CharField(
        max_length=50, help_text="Nome Fantasia da empresa")
    CNPJ = BRCNPJField(max_length=18, help_text="CNPJ da empresa",
                       verbose_name="CNPJ da empresa")
    Email_Principal = models.EmailField(
        max_length=100, help_text="Email do responsável", verbose_name="Email")
    Data_Cadastro = models.DateField(
        auto_now_add=True, verbose_name="Data de Cadastro", db_index=True)
    Endereco = models.OneToOneField(
        Endereco, on_delete=models.SET_NULL, null=True)
    Inativo = models.BooleanField(default=False, verbose_name="Inativo")

    def __init__(self, *args, **kwargs):
        self.queryset = Empresa.objects.filter(Inativo=False)
        super(Empresa, self).__init__(*args, **kwargs)

    def __str__(self) -> str:
        return self.Razao_Social

    class Meta:
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"
