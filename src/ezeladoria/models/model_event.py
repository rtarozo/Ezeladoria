# flake8: noqa
from django.db import models

#from .model_adress import Endereco
#from .model_company import Empresa
from .model_envet_type import TipoEvento


class Evento(models.Model):
    STATUS_CHOICES = (
        ("0", "Enviado"),
        ("1", "Recebido"),
        ("2", "Em Analise"),
        ("3", "Encaminhado"),
        ("4", "Aguardando Solução"),
        ("5", "Cancelado"),
        ("6", "Resolvido"),
    )
    Evento_Id = models.AutoField(primary_key=True, verbose_name="Sequencia")
    Data_Cadastro = models.DateField(
        "Data de Cadastro", auto_now_add=True, db_index=True)
    Longitude = models.FloatField(
        null=False, blank=False, default=0.0, editable=True)
    Latitude = models.FloatField(
        null=False, blank=False, default=0.0, editable=True)
    Foto = models.ImageField(upload_to="", max_length=None, blank=True, null=True)
    #Foto = models.Base64ImageFild(upload_to="medias/")
    Status = models.CharField(
        max_length=2, choices=STATUS_CHOICES, blank=False, null=False)
    Tipo_Evento_Id = models.ForeignKey(TipoEvento, on_delete=models.CASCADE)
    #Endrereco = models.ForeignKey(
    #    Endereco, on_delete=models.SET_NULL, blank=True, null=True)
    Endrereco = models.BigIntegerField(blank=True, null=True)
    
    class Meta:
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"
