from django.shortcuts import render
# Importa a função HttpResponse do módulo django.http
from django.http import HttpResponse

# Define uma função de visualização chamada 'index'
def index(response):
    # Retorna uma resposta HTTP contendo um título HTML
    return HttpResponse("<h1> Hello World </h1>")

# Define outra função de visualização chamada 'v1'
def v1(response):
    # Retorna uma resposta HTTP contendo um título HTML diferente
    return HttpResponse("<h1> v1 page </h1>")