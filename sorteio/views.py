from django.shortcuts import render
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