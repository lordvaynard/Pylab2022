from django.urls import path
from . import views

urlpatterns = [
    path('nova_vaga/', views.nova_vaga, name="nova_vaga")
]
