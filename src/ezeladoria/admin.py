from django.contrib import admin

from .models.model_account import ContaCorrente
from .models.model_account_entry import LancamentoConta
from .models.model_adress import Endereco
from .models.model_bank import Banco
from .models.model_bank_account import ContaBanco
from .models.model_company import Empresa
from .models.model_default_historic import HistoricoPadrao
from .models.model_envet_type import TipoEvento
from .models.model_event import Evento
from .models.model_parameters import Parametro
from .models.model_responsible_body import Orgao_Responsavel


@admin.register(ContaCorrente)
class ContaCorrenteAdmin(admin.ModelAdmin):
    list_per_page: int = 20
    search_fields = ("Codigo_Conta__conteins", "Tipo_Conta__contains")
    ordering = ("Tipo_Conta",)
    readonly_fields = (
        "Saldo",
        "Limite_Credito",
    )
    list_display = (
        "Tipo_Conta",
        "Codigo_Conta",
        "Digito_Conta",
        "Saldo",
        "Limite_Credito",
    )
    list_filter = ("Tipo_Conta",)

@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_per_page: int = 20
    search_fields = (
        "Razao_Social__conteins",
        "Nome_Fantasia__contains",
        "CNPJ_contains",
    )
    ordering = ("Razao_Social",)
    list_display = (
        "Razao_Social",
        "Nome_Fantasia",
    )


@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    list_per_page: int = 20
    search_fields = (
        "Logradouro__conteins",
        "Cidade__contains",
        "Estado_contains",
    )
    ordering = (
        "Estado",
        "Cidade",
    )
    list_display = (
        "Pais",
        "Estado",
        "Cidade",
        "Logradouro",
        "Numero",
        "Complemento",
        "Bairro",
    )
    list_filter = (
        "Pais",
        "Estado",
        "Cidade",
    )


class EventoInLine(admin.StackedInline):
    model = Evento
    extra = 3


@admin.register(TipoEvento)
class TipoEventoAdmin(admin.ModelAdmin):
    inlines = [EventoInLine]    


admin.site.register(LancamentoConta)
admin.site.register(HistoricoPadrao)
admin.site.register(Banco)
admin.site.register(ContaBanco)
admin.site.register(Parametro)
admin.site.register(Evento)
admin.site.register(Orgao_Responsavel)