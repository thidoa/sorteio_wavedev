from django.shortcuts import render
from .models import Participante
from django.core.mail import send_mail
import schedule
import time
import threading
import random
# from django.utils import timezone
from datetime import datetime, timezone
from .models import Participante
# Create your views here.

def index(request):
    return render(request, 'index.html')

def sorteios(request):
    return render(request, 'sorteios.html')

def participar_sorteio(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        cidade = request.POST['cidade']
        telefone = request.POST['telefone']
        email = request.POST['email']

        participante = Participante.objects.create(nome=nome, cidade=cidade, telefone=telefone, email=email)
        participante.save()
    return render(request, 'sorteios.html')


def listar(request):
    participantes = Participante.objects.all()

    context = {
        'participantes': participantes,
    }

    return render(request, 'listar.html', context)


def sorteado(request):
    sorteado = open("templates/sorteado.txt", "r")
    info_sorteado = sorteado.read()
    
    if len(info_sorteado) == 0:
        mensagem = 'Sorteio não realizado'
    else:
        mensagem = ''

    context = {
        'sorteado': info_sorteado.split("\n"),
        'mensagem': mensagem,
    }

    return render(request, 'sorteado.html', context)

def realizar_sorteio(request):
    participantes = Participante.objects.all() 
    sorteado = random.choice(participantes)

    send_mail('Sorteio', 'Você foi sorteado, parabens', 'thiagovini200@gmail.com', [f'{sorteado.email}'])

    with open("templates/sorteado.txt", "w") as arquivo:
        arquivo.write(f"{sorteado.nome}\n{sorteado.cidade}\n{sorteado.telefone}\n{sorteado.email}")
    
    print(f"Sorteado foi {sorteado}")


def agendar_sorteio(data_sorteio, sorteio_id):
    # Agenda a execução da função realizar_sorteio para a data e hora definidas
    schedule.every().day.at(data_sorteio.strftime('%H:%M:%S')).do(realizar_sorteio, sorteio_id)
    
    while True:
        schedule.run_pending()
        time.sleep(1)
    
# Agenda a execução da função de sorteio para a data e hora definidas
data_sorteio = datetime(2023, 3, 27, 18, 0, 0)

# Cria um thread para agendar o sorteio
thread = threading.Thread(target=agendar_sorteio, args=(data_sorteio, 10))

# Inicia a execução do thread
thread.start()

def sorteio(request):
    return render(request, 'sorteio.html')

def sobre(request):
    return render(request, 'sobre.html')

