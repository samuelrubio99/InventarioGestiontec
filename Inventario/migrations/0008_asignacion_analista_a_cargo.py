# Generated by Django 4.1.3 on 2022-11-21 22:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Inventario', '0007_analista_gestion_remove_asignacion_acta_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='asignacion',
            name='Analista_a_Cargo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Inventario.analista_gestion'),
        ),
    ]
