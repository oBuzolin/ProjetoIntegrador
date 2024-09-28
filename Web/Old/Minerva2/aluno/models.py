from django.db import models

class Minerva_Aluno(models.Model):
    ra = models.AutoField(primary_key=True)  # Usando AutoField para RA como chave primária
    nome = models.CharField(max_length=100)
    usuario = models.EmailField(max_length=255, unique=True)  # Usando EmailField para garantir a unicidade e formato
    senha = models.CharField(max_length=255)
    curso = models.CharField(max_length=100)

    def __str__(self):
        return f'Aluno {self.nome} - RA: {self.ra}'

    class Meta:
        db_table = 'Minerva_Aluno'
        managed = False
