from django.db import models
from django.contrib.auth.models import User

class SalaDeAula(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return self.nome
    
class Mensagem(models.Model):
    sala = models.ForeignKey(SalaDeAula, on_delete=models.CASCADE, related_name="mensagens")
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.TextField()
    data_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.usuario.username}: {self.texto[:100]}'

# Create your models here.
