from django.contrib import admin
from .models import Tecnologias, Empresa, Vagas
#tudo inserido aqui fica disponivel no admin do Django
admin.site.register(Tecnologias)
admin.site.register(Empresa)
admin.site.register(Vagas)