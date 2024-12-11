from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password
from aluno.models import Minerva_Aluno
from django.utils import timezone

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


class Minerva_Turma(models.Model):
    id_Turma = models.AutoField(primary_key=True)
    nomeTurma = models.CharField(max_length=100)

    class Meta:
        db_table = 'Minerva_Turma'
        managed = False


class Minerva_MatriculaTurma(models.Model):
    ra = models.ForeignKey(Minerva_Aluno, on_delete=models.CASCADE)
    id_Turma = models.ForeignKey(Minerva_Turma, on_delete=models.CASCADE)
    dataMatricula = models.DateField()

    class Meta:
        db_table = 'Minerva_MatriculaTurma'
        managed = False


class Minerva_ProfessorTurma(models.Model):
    id = models.AutoField(primary_key=True, )  # Chave primária
    matricula = models.ForeignKey(Minerva_Professor, on_delete=models.CASCADE, db_column='matricula')
    id_Turma = models.ForeignKey(Minerva_Turma, on_delete=models.CASCADE, db_column='id_Turma')

    class Meta:
        db_table = 'Minerva_ProfessorTurma'
        managed = False

class Minerva_Disciplina(models.Model):
    id_Turma = models.ForeignKey(Minerva_Turma, on_delete=models.CASCADE)
    nome_disciplina = models.CharField(max_length=100)

    class Meta:
        db_table = 'Minerva_Disciplina'
        managed = False

class Minerva_MuralMensagem(models.Model):
    id = models.AutoField(primary_key=True)
    aluno = models.ForeignKey(Minerva_Aluno, null=True, blank=True, on_delete=models.SET_NULL)
    professor = models.ForeignKey(Minerva_Professor, null=True, blank=True, on_delete=models.SET_NULL)
    mensagem = models.TextField()
    data_publicacao = models.DateTimeField(default=timezone.now)
    turma = models.ForeignKey('Minerva_Turma', on_delete=models.CASCADE)
    

    def __str__(self):
        if self.aluno:
            return f"Mensagem de {self.aluno.nome}"
        elif self.professor:
            return f"Mensagem de {self.professor.nome}"
        return "Mensagem sem autor"

    class Meta:
        db_table = 'Minerva_MuralMensagem'
        managed = False