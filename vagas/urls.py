from django.urls import path
from . import views

urlpatterns = [
    path('nova_vaga/', views.nova_vaga, name="nova_vaga"),
    path('vaga/<int:id>', views.vaga, name="vaga"),
    path('nova_tarefa/<int:id_vaga>', views.nova_tarefa, name='nova_tarefa'),
    path('realizar_tarefa/<int:id>', views.realizar_tarefa, name='realizar_tarefa'),
    path('envia_email/<int:id_vaga>', views.envia_email, name="envia_email"),
]
