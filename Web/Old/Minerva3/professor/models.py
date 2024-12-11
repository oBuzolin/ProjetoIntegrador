from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password

class Minerva_Professor(models.Model):
    matricula = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    usuario = models.EmailField(max_length=255, unique=True)
    senha = models.CharField(max_length=255)
    disciplina = models.CharField(max_length=100)
    cargaHoraria = models.IntegerField()
    diaSemana = models.CharField(max_length=100)

    def set_senha(self, raw_password):
        self.senha = make_password(raw_password)
        self.save()

    def check_senha(self, raw_password):
        return check_password(raw_password, self.senha)

    def __str__(self):
        return f'Professor {self.nome} - Matrícula: {self.matricula}'

    class Meta:
        db_table = 'Minerva_Professor'
        managed = False

class SalaAula(models.Model):
    nome = models.CharField(max_length=100)
    materia = models.ForeignKey('Materia', on_delete=models.CASCADE)
    turma = models.CharField(max_length=50)
    professor = models.ForeignKey(Minerva_Professor, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nome} - {self.turma}"

class Materia(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
    
class Mensagem(models.Model):
    sala = models.ForeignKey(SalaAula, on_delete=models.CASCADE, related_name="mensagens")
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.TextField()
    data_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.usuario.username}: {self.texto[:100]}'

# Create your models here. 
