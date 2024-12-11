# Generated by Django 4.2.13 on 2024-09-29 19:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('professor', '0005_matricula_turma_professorturma_teste_turma_teste'),
    ]

    operations = [
        migrations.CreateModel(
            name='Disciplina_Teste',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_disciplina', models.CharField(max_length=100)),
                ('id_Turma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='professor.turma_teste')),
            ],
            options={
                'db_table': 'Disciplina_Teste',
                'managed': True,
            },
        ),
    ]