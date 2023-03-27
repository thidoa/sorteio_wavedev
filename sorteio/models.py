from django.db import models

# Create your models here.

class Participante(models.Model):
    nome = models.CharField(max_length=200)
    estado = models.CharField(max_length=200)
    telefone = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

    def __str__(self):
        return self.nome