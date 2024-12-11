# Generated by Django 4.2.13 on 2024-10-27 15:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Minerva_Disciplina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_disciplina', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'Minerva_Disciplina',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Minerva_MatriculaTurma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataMatricula', models.DateField()),
            ],
            options={
                'db_table': 'Minerva_MatriculaTurma',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Minerva_MuralMensagem',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('mensagem', models.TextField()),
                ('data_publicacao', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'Minerva_MuralMensagem',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Minerva_Professor',
            fields=[
                ('matricula', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100)),
                ('usuario', models.EmailField(max_length=255, unique=True)),
                ('senha', models.CharField(max_length=255)),
                ('disciplina', models.CharField(max_length=100)),
                ('cargaHoraria', models.IntegerField()),
                ('diaSemana', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'Minerva_Professor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Minerva_ProfessorTurma',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'Minerva_ProfessorTurma',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Minerva_Turma',
            fields=[
                ('id_Turma', models.AutoField(primary_key=True, serialize=False)),
                ('nomeTurma', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'Minerva_Turma',
                'managed': False,
            },
        ),
    ]
