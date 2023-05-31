# flake8: noqa
from django.db import models


class Fatura(models.Model):
    TIPO_CHOICES = (
        ("1", "Avulsa"),
        ("2", "Mensal"),
        ("3", "Anual"),
    )
    pass
