# users/models.py

from django.db import models
from professor.models import Minerva_Professor

class Minerva_Login(models.Model):
    id = models.AutoField(primary_key=True)
    # adm_matricula = models.ForeignKey('Minerva_Administrador', on_delete=models.CASCADE, null=True, blank=True)
    professor_matricula_id = models.ForeignKey('professor.Minerva_Professor', on_delete=models.CASCADE, null=True, blank=True, db_column='professor_matricula')
    aluno_ra_id = models.ForeignKey('aluno.Minerva_Aluno', on_delete=models.CASCADE, null=True, blank=True, db_column='aluno_ra')
    status = models.CharField(max_length=20, choices=[('ativo', 'Ativo'), ('cancelado', 'Cancelado'), ('bloqueado', 'Bloqueado')])

    def __str__(self):
        return f'Login {self.id} - Status: {self.status}'
    
    class Meta:
        # db_table = 'Minerva_Login'
        db_table = 'Minerva_Login'
        managed = False  # Evita que o Django tente criar ou alterar essa tabela
