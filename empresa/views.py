from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.messages import constants
from .models import Tecnologias, Empresa


def nova_empresa(request):
    url_atual = '/home/nova_empresa'
    if request.method == "GET":  # se requisição veio do navegador
        techs = Tecnologias.objects.all()  # consulta no banco de dados as tecnologias
        # passando o retorno do SQL para o template
        return render(request, 'nova_empresa.html', {'techs': techs})
    elif request.method == "POST":  # se requisição veio do formulario
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        cidade = request.POST.get('cidade')
        endereco = request.POST.get('endereco')
        nicho = request.POST.get('nicho')
        caracteristicas = request.POST.get('caracteristicas')
        tecnologias = request.POST.getlist('tecnologias')
        logo = request.FILES.get('logo')

        #verifica campos em branco
        if (len(nome.strip()) == 0 or len(email.strip()) == 0 or len(cidade.strip()) == 0 or len(endereco.strip()) == 0 or len(nicho.strip()) == 0 or len(caracteristicas.strip()) == 0 or (not logo)):
            messages.add_message(request, constants.ERROR, 'Preencha todos os campos')
            return redirect(url_atual)

        #verififca se a logo tem até 10mb
        if logo.size > 100_000_000:
            messages.add_message(request, constants.ERROR,'A logo da empresa deve ter menos de 10MB')
            return redirect(url_atual)

        #verifica se o nicho existe na empresa
        if nicho not in [i[0] for i in Empresa.choices_nicho_mercado]:
            messages.add_message(request, constants.ERROR, 'Nicho de mercado inválido')
            return redirect(url_atual)
        
        empresa = Empresa(logo=logo,
                        nome=nome,
                        email=email,
                        cidade=cidade,
                        endereco=endereco,
                        nicho_mercado=nicho,
                        caracteristicas_empresa=caracteristicas)
        empresa.save()
        empresa.tecnologias.add(*tecnologias)
        empresa.save()
        messages.add_message(request, constants.SUCCESS, 'Empresa cadastrada com sucesso')
        return redirect(url_atual)        

def empresa(request):
    empresas = Empresa.objects.all() #select de todas empresas cadastradas
    return render(request, 'empresa.html', {'empresas': empresas}) #passando o resultado do select como parametro para o template

def excluir_empresa(request, id):
    url_atual = '/home/empresa'
    empresa = Empresa.objects.get(id=id)
    empresa.delete()
    messages.add_message(request, constants.SUCCESS, 'Empresa excluida com sucesso')
    return redirect(url_atual)  