# Generated by Django 4.2.13 on 2024-08-30 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_user_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Minerva_Login',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.CharField(choices=[('ativo', 'Ativo'), ('cancelado', 'Cancelado'), ('bloqueado', 'Bloqueado')], max_length=20)),
            ],
            options={
                'db_table': 'Minerva_Login',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
