# Generated by Django 4.1.3 on 2022-11-22 00:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Inventario', '0015_rename_backup_laptop_ultimo_backup'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cargador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Modelo', models.CharField(max_length=30)),
                ('Estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventario.estado')),
                ('Marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventario.marca')),
            ],
            options={
                'verbose_name_plural': 'Cargador',
            },
        ),
    ]
