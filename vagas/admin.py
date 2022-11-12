from django.contrib import admin

# Register your models here.
from .models import Tarefa, Emails
#tudo inserido aqui fica disponivel no admin do Django
admin.site.register(Tarefa)
admin.site.register(Emails)