# Generated by Django 4.2.13 on 2024-11-17 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('professor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Minerva_Atividades',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=100)),
                ('escopo', models.CharField(max_length=500)),
                ('envio', models.DateTimeField()),
                ('entrega', models.DateTimeField(default=None, null=True)),
                ('nota', models.DecimalField(blank=True, decimal_places=2, max_digits=4)),
                ('caminho_arquivo', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'Minerva_Atividades',
                'managed': False,
            },
        ),
    ]
