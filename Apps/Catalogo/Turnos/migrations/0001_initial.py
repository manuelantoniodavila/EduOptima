# Generated by Django 4.2.16 on 2024-09-12 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Turnos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CodigoModalidad', models.CharField(max_length=35)),
                ('NombreModalidad', models.CharField(max_length=25)),
                ('Horario_Clases', models.CharField(max_length=10)),
            ],
        ),
    ]
