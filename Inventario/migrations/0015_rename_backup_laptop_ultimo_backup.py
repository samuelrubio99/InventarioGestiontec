# Generated by Django 4.1.3 on 2022-11-22 00:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Inventario', '0014_tarjeta_grafica'),
    ]

    operations = [
        migrations.RenameField(
            model_name='laptop',
            old_name='Backup',
            new_name='Ultimo_Backup',
        ),
    ]
