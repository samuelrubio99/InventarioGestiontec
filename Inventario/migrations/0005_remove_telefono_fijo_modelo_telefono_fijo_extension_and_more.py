# Generated by Django 4.1.3 on 2022-11-21 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventario', '0004_remove_licencia_modelo_licencia_software'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='telefono_fijo',
            name='Modelo',
        ),
        migrations.AddField(
            model_name='telefono_fijo',
            name='Extension',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='motherboard',
            name='Serial',
            field=models.CharField(max_length=40, unique=True),
        ),
    ]
