from django.db.models.signals import post_save

from ezeladoria.models.model_account import CriaConta
from ezeladoria.models.model_company import Empresa

post_save.connect(CriaConta, sender=Empresa)
