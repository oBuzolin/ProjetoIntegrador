# users/models.py
from django.db import models

class User(models.Model):
    usuario = models.EmailField(primary_key=True, max_length=255)
    senha = models.CharField(max_length=255)
    cargo = models.IntegerField()

    class Meta:
        db_table = 'Minerva_Login'
        managed = False  # Evita que o Django tente criar ou alterar essa tabela
