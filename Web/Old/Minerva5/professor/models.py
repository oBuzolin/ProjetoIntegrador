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


class Turma_Teste(models.Model):
    id_Turma = models.AutoField(primary_key=True)
    nomeTurma = models.CharField(max_length=100)

    class Meta:
        db_table = 'Turma_Teste'
        managed = False


class Matricula_Turma(models.Model):
    ra = models.ForeignKey(Minerva_Aluno, on_delete=models.CASCADE)
    id_Turma = models.ForeignKey(Turma_Teste, on_delete=models.CASCADE)
    dataMatricula = models.DateField()

    class Meta:
        db_table = 'Matricula_Turma'
        managed = False


class ProfessorTurma_Teste(models.Model):
    id = models.AutoField(primary_key=True, )  # Chave primária
    matricula = models.ForeignKey(Minerva_Professor, on_delete=models.CASCADE, db_column='matricula')
    id_Turma = models.ForeignKey(Turma_Teste, on_delete=models.CASCADE, db_column='id_Turma')

    class Meta:
        db_table = 'ProfessorTurma_Teste'
        managed = False

class Disciplina_Teste(models.Model):
    id_Turma = models.ForeignKey(Turma_Teste, on_delete=models.CASCADE)
    nome_disciplina = models.CharField(max_length=100)

    class Meta:
        db_table = 'Disciplina_Teste'
        managed = False

class MuralMensagem_Teste(models.Model):
    id = models.AutoField(primary_key=True)
    aluno_id = models.ForeignKey(Minerva_Aluno, null=True, blank=True, on_delete=models.SET_NULL)
    professor_id = models.ForeignKey(Minerva_Professor, null=True, blank=True, on_delete=models.SET_NULL)
    mensagem = models.TextField()
    data_publicacao = models.DateTimeField(default=timezone.now)
    id_Turma = models.ForeignKey('Turma_Teste', on_delete=models.CASCADE)

    def __str__(self):
        if self.aluno_id:
            return f"Mensagem de {self.aluno_id.nome}"
        elif self.professor_id:
            return f"Mensagem de {self.professor_id.nome}"
        return "Mensagem sem autor"
    
    # def save(self, *args, **kwargs):
    #     if not self.aluno and not self.professor:
    #         raise ValueError("A mensagem deve ter um aluno ou um professor como autor.")
    #     super().save(*args, **kwargs)
    
    class Meta:
        db_table = 'MuralMensagem_Teste'
        managed = False