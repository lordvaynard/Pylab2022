# Ativando o projeto Python
& d:/Work/Projetos/Pylab2022/venv/Scripts/Activate.ps1

# Se (venv) no console, executar abaixo
python manage.py runserver

# acessar pagina de empresas
http://127.0.0.1:8000/home/empresa/

# cria os modelos conforme o models.py
python manage.py makemigrations 

# executa as migrações no banco
python manage.py migrate 