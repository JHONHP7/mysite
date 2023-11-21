from django.shortcuts import render

# Importa a função HttpResponse do módulo django.http
from django.http import HttpResponse
from .models import ToDoList, Item


# Define uma função de visualização chamada 'index'
def index(response, id):
    ls = ToDoList.objects.get(id=id)
    my_dict = {"name": ls.name, "items": list(ls.item_set.filter(text__contains="Go"))}
    # Retorna uma resposta HTTP contendo um título HTML
    return render(
        response,
        "main/list.html",
        {"ls": ls},
    )


def home(response):
    return render(response, "main/home.html", {})
