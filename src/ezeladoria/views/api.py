# flake8: noqa
from rest_framework import generics

from ezeladoria.models.model_envet_type import TipoEvento
from ezeladoria.models.model_event import Evento
from ezeladoria.serializers import EventoSerializer, TipoEventoSerializer

# from rest_framework.decorators import api_view
# from rest_framework.response import Response


class TiposEventosAPIView(generics.ListCreateAPIView):
    queryset = TipoEvento.objects.all()
    serializer_class = TipoEventoSerializer


class TipoEventoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TipoEvento.objects.all()
    serializer_class = TipoEventoSerializer


class EventosAPIView(generics.ListCreateAPIView):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer


class EventoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer
