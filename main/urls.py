# Importa a função 'path' do módulo django.urls e as funções de visualização do aplicativo
from django.urls import path
from . import views

# Lista de padrões de URL associados a funções de visualização
urlpatterns = [
    # Mapeia a URL raiz para a função 'index' no arquivo 'views.py'
    path("<str:name>", views.index, name="index"),
]
