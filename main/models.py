from django.db import models
# Em Django, os modelos são usados para definir a estrutura das tabelas no banco de dados. 
# Cada modelo é uma classe que herda de django.db.models.Model. Cada atributo do modelo representa um campo de banco de dados. 
# Com base nos modelos, o Django cria automaticamente um esquema de banco de dados (CREATE TABLE SQL) para armazenar os dados dos objetos Python.

# Create your models here.
class ToDoList(models.Model):
    name = models.CharField(max_length=200) # como no spring vc está criando uma classe de um objeto que irá ser persistido no banco de dados

    def __str__(self):
        return self.name
    
class Item(models.Model):
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE) # o on_delete é para caso vc delete uma lista, os itens dela tbm sejam deletados
    text = models.CharField(max_length=300)
    complete = models.BooleanField()

    def __str__(self):
        return self.text