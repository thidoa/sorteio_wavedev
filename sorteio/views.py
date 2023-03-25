from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def sorteio(request):
    return render(request, 'sorteio.html')

def sobre(request):
    return render(request, 'sobre.html')