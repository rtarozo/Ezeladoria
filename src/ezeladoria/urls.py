from django.urls import path

from .views import views
from .views.api import (EventoAPIView, EventosAPIView, TipoEventoAPIView,
                        TiposEventosAPIView)

app_name = 'ezeladoria'
urlpatterns = [
    path("tipos-evento/", TiposEventosAPIView.as_view(), name="tipos-evento"),
    path("tipo-evento/<int:pk>", TipoEventoAPIView.as_view(), name="tipo-evento"),
    path("eventos/", EventosAPIView.as_view(), name="eventos"),
    path("evento/<int:pk>", EventoAPIView.as_view(), name="evento"),
    path('', views.IndexView.as_view(), name='index'),
]
