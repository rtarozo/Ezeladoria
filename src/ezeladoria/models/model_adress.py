# flake8: noqa
from django.db import models
from localflavor.br.models import BRPostalCodeField, BRStateField


class Endereco(models.Model):
    """
    ESTADO_CHOICES = (
        ("AC", "Acre"),
        ("AL", "Alagoas"),
        ("AP", "Amapá"),
        ("AM", "Amazonas"),
        ("BA", "Bahia"),
        ("CE", "Ceará"),
        ("DF ", "Distrito Federal"),
        ("ES", "Espírito Santo"),
        ("GO", "Goiás"),
        ("MA", "Maranhão"),
        ("MT", "Mato Grosso"),
        ("MS", "Mato Grosso do Sul"),
        ("MG", "Minas Gerais"),
        ("PA", "Pará"),
        ("PB", "Paraíba"),
        ("PR", "Paraná"),
        ("PE", "Pernambuco"),
        ("PI", "Piauí"),
        ("RJ", "Rio de Janeiro"),
        ("RN", "Rio Grande do Norte"),
        ("RS", "Rio Grande do Sul"),
        ("RO", "Rondônia"),
        ("RR", "Roraima"),
        ("SC", "Santa Catarina"),
        ("SP", "São Paulo"),
        ("SE", "Sergipe"),
        ("TO", "Tocantins"),
    )
    """

    Logradouro = models.CharField(max_length=100, null=False, blank=False)
    Numero = models.CharField(max_length=15, null=True, blank=True)
    Complemento = models.CharField(max_length=40, null=True, blank=True)
    # Estado = models.CharField(max_length=3, choices=ESTADO_CHOICES, blank=False, null=False, default="SP")
    Estado = BRStateField(max_length=3, blank=False, null=False, default="SP")
    Bairro = models.CharField(max_length=50, null=False, blank=False)
    Cidade = models.CharField(max_length=100, null=False, blank=False)
    Pais = models.CharField(max_length=50, null=False, blank=False)
    CEP = BRPostalCodeField(max_length=9, null=False, blank=False)

    def __str__(self):
        return self.Logradouro

    class Meta:
        verbose_name = "Endereço"
        verbose_name_plural = "Endereços"
