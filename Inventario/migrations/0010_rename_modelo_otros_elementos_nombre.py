# Generated by Django 4.1.3 on 2022-11-21 22:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Inventario', '0009_rename_periferico_otros_elementos'),
    ]

    operations = [
        migrations.RenameField(
            model_name='otros_elementos',
            old_name='Modelo',
            new_name='Nombre',
        ),
    ]
