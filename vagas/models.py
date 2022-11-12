from django.db import models
from empresa.models import Vagas
from django.utils.safestring import mark_safe

class Tarefa(models.Model):
    choices_prioridade = (
        ('B', 'Baixa'),
        ('A', 'Alta'),
        ('U', 'Urgente')
    )
    vaga = models.ForeignKey(Vagas, on_delete=models.CASCADE) #se excluir a vaga esclui as tarefas
    titulo = models.CharField(max_length=30)
    prioridade = models.CharField(max_length=1, choices=choices_prioridade)
    data = models.DateField()
    realizada = models.BooleanField(default=False)
    
    def icon(self):
        if self.prioridade == "U":
            classe = 'prioridade-vermelho'
        elif self.prioridade == "A":
            classe = 'prioridade-amarelo'
        elif self.prioridade == "B":
            classe = 'prioridade-verde'

        icon = f'''<svg  class="{classe}" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-exclamation-triangle-fill" viewBox="0 0 16 16">
                      <path d="M8.982 1.566a1.13 1.13 0 0 0-1.96 0L.165 13.233c-.457.778.091 1.767.98 1.767h13.713c.889 0 1.438-.99.98-1.767L8.982 1.566zM8 5c.535 0 .954.462.9.995l-.35 3.507a.552.552 0 0 1-1.1 0L7.1 5.995A.905.905 0 0 1 8 5zm.002 6a1 1 0 1 1 0 2 1 1 0 0 1 0-2z"/>
                   </svg>'''

        return mark_safe(icon)
        

    def __str__(self):
        return self.titulo
    
class Emails(models.Model):
    vaga = models.ForeignKey(Vagas, on_delete=models.DO_NOTHING)
    assunto = models.CharField(max_length=100)
    corpo = models.TextField()
    enviado = models.BooleanField()

    def __str__(self):
        return self.assunto