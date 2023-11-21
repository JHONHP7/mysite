from django.contrib import admin
from .models import ToDoList, Item
# Register your models here.
admin.site.register(ToDoList) # aqui vc registra os modelos para que eles apareçam no admin do django
admin.site.register(Item) # aqui vc registra os modelos para que eles apareçam no admin do django