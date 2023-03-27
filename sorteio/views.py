from django.shortcuts import render, redirect
from .models import Participante
from django.core.mail import send_mail
import random
# Create your views here.

def index(request):
    print(request.user.is_superuser)
    return render(request, 'index.html')

def sorteio(request):
    sorteado = open("templates/sorteado.txt", "r")
    info_sorteado = sorteado.read()
    
    if len(info_sorteado) == 0:
        foi_sorteado = False
    else:
        foi_sorteado = True

    context = {
        'foi_sorteado': foi_sorteado,
        'sorteado': info_sorteado.split("\n"),
    }

    return render(request, 'sorteio.html', context)

def sobre(request):
    return render(request, 'sobre.html')

def participar_sorteio(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        estado = request.POST['estado']
        telefone = request.POST['telefone']
        email = request.POST['email']

        participante = Participante.objects.create(nome=nome, estado=estado, telefone=telefone, email=email)
        participante.save()

    return render(request, 'sorteio.html')

def realizar_sorteio(request):
    participantes = Participante.objects.all() 
    sorteado = random.choice(participantes)

    send_mail('Sorteio', 'Você foi sorteado, parabens', 'thiagovini200@gmail.com', [f'{sorteado.email}'])

    with open("templates/sorteado.txt", "w") as arquivo:
        arquivo.write(f"{sorteado.nome}\n{sorteado.estado}\n{sorteado.telefone}\n{sorteado.email}")
    
    print(f"Sorteado foi {sorteado}")
    return redirect('sorteio')
