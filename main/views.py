from django.shortcuts import render
# Importa a função HttpResponse do módulo django.http
from django.http import HttpResponse
from .models import ToDoList, Item

# Define uma função de visualização chamada 'index'
def index(response, name):
    ls = ToDoList.objects.get(name=name)
    item = ls.item_set.get(id=1)
    # Retorna uma resposta HTTP contendo um título HTML
    return HttpResponse("<h1>%s</h1><br><p>%s</p>" %(ls.name, str(item.text)))

