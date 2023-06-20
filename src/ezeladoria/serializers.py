from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers

from ezeladoria.models.model_envet_type import TipoEvento
from ezeladoria.models.model_event import Evento


class EventoSerializer(serializers.ModelSerializer):
    Foto = Base64ImageField(required=False)
    
    class Meta:
        model = Evento
        fields = "__all__"
        
    def create(self, validated_data):
        Foto = validated_data.pop('Foto')
        created_item = Evento.objects.create(**validated_data)
        created_item.Foto = Foto
        created_item.save()
        return True
    
    """ precisa 
    '1 - pegar o cep pela longitude e latitude 
    '2 - gravar na tabela endereço
    '3 - pegar o id do registro gravado
    '4 - gravar no campo endereço
    def validate_Endereco(sef, valor):
        if not valor:
            get_cep
    """


class TipoEventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoEvento
        fields = ("Tipo_Evento_Id", "Descricao")
