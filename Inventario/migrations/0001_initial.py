# Generated by Django 4.1.3 on 2022-11-10 05:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Acta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tipo', models.CharField(max_length=20, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Acta',
            },
        ),
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Area', models.CharField(max_length=40, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Area',
            },
        ),
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cargo', models.CharField(max_length=40, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Cargo',
            },
        ),
        migrations.CreateModel(
            name='Disco_Duro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Serial', models.CharField(max_length=15, unique=True)),
                ('Tipo', models.CharField(max_length=5)),
                ('Capacidad', models.CharField(max_length=5)),
            ],
            options={
                'verbose_name_plural': 'Disco_Duro',
            },
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Estado', models.CharField(max_length=20, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Estado',
            },
        ),
        migrations.CreateModel(
            name='Licencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=60, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Licencia',
            },
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Marca',
            },
        ),
        migrations.CreateModel(
            name='Procesador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Modelo', models.CharField(max_length=100)),
                ('Estructura', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Procesador',
            },
        ),
        migrations.CreateModel(
            name='VoIP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Modelo', models.CharField(max_length=40)),
                ('Direccion_IP', models.CharField(max_length=30, unique=True)),
                ('Direccion_Mac', models.CharField(max_length=30, unique=True)),
                ('Extencion_Telefono', models.CharField(max_length=50)),
                ('Observacion', models.CharField(max_length=100)),
                ('Area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventario.area')),
            ],
            options={
                'verbose_name_plural': 'VoIP',
            },
        ),
        migrations.CreateModel(
            name='Telefono_fijo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Serial', models.CharField(max_length=15, unique=True)),
                ('Modelo', models.CharField(max_length=30)),
                ('Direccion_mac', models.CharField(max_length=30)),
                ('Observacion', models.TextField(max_length=200)),
                ('Estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventario.estado')),
                ('Marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventario.marca')),
            ],
            options={
                'verbose_name_plural': 'Telefono_fijo',
            },
        ),
        migrations.CreateModel(
            name='Teclado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Serial', models.CharField(max_length=15, unique=True)),
                ('Modelo', models.CharField(max_length=30)),
                ('Observacion', models.TextField(max_length=200)),
                ('Estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventario.estado')),
                ('Marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventario.marca')),
            ],
            options={
                'verbose_name_plural': 'Teclado',
            },
        ),
        migrations.CreateModel(
            name='Tablet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Serial', models.CharField(max_length=30, unique=True)),
                ('Modelo', models.CharField(max_length=200)),
                ('Direccion_Mac', models.CharField(max_length=30, unique=True)),
                ('Version_SO', models.CharField(default='', max_length=30)),
                ('Cargador', models.CharField(max_length=200)),
                ('Observacion', models.TextField(max_length=200)),
                ('Acta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventario.acta')),
                ('Estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventario.estado')),
                ('Marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventario.marca')),
            ],
            options={
                'verbose_name_plural': 'Tablet',
            },
        ),
        migrations.CreateModel(
            name='Ram',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Serial', models.CharField(max_length=15, unique=True)),
                ('Modelo', models.CharField(max_length=30)),
                ('Capacidad', models.CharField(max_length=5)),
                ('Marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventario.marca')),
            ],
            options={
                'verbose_name_plural': 'Ram',
            },
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombres', models.CharField(max_length=200)),
                ('Apellidos', models.CharField(max_length=200)),
                ('Correo', models.EmailField(max_length=100, unique=True)),
                ('Numero_Celular', models.CharField(default='', max_length=70)),
                ('Area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventario.area')),
            ],
            options={
                'verbose_name_plural': 'Persona',
            },
        ),
        migrations.CreateModel(
            name='Periferico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Serial', models.CharField(max_length=15, unique=True)),
                ('Modelo', models.CharField(max_length=30)),
                ('Cantidad', models.IntegerField(blank=True, null=True)),
                ('Observacion', models.TextField(max_length=200)),
                ('Estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventario.estado')),
                ('Marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventario.marca')),
            ],
            options={
                'verbose_name_plural': 'Periferico',
            },
        ),
        migrations.CreateModel(
            name='Mouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Serial', models.CharField(max_length=15, unique=True)),
                ('Observacion', models.TextField(max_length=200)),
                ('Estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventario.estado')),
            ],
            options={
                'verbose_name_plural': 'Mouse',
            },
        ),
        migrations.CreateModel(
            name='Motherboard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Serial', models.CharField(max_length=15, unique=True)),
                ('Estructura', models.CharField(max_length=200)),
                ('Marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventario.marca')),
            ],
            options={
                'verbose_name_plural': 'Motherboard',
            },
        ),
        migrations.CreateModel(
            name='Monitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Serial', models.CharField(max_length=15, unique=True)),
                ('Modelo', models.CharField(max_length=30)),
                ('Observacion', models.TextField(max_length=200)),
                ('Estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventario.estado')),
                ('Marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventario.marca')),
            ],
            options={
                'verbose_name_plural': 'Monitor',
            },
        ),
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Serial', models.CharField(max_length=30, unique=True)),
                ('Modelo', models.CharField(max_length=80)),
                ('Tarjeta_Grafica', models.CharField(max_length=80)),
                ('LAN_MAC', models.CharField(max_length=30, unique=True)),
                ('WLAN_MAC', models.CharField(max_length=30, unique=True)),
                ('Backup', models.DateField(blank=True, null=True)),
                ('Cargador', models.CharField(max_length=80)),
                ('Bateria', models.CharField(max_length=80)),
                ('Observacion', models.TextField(max_length=200)),
                ('Acta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventario.acta')),
                ('Disco_Duro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventario.disco_duro')),
                ('Estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventario.estado')),
                ('Licencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventario.licencia')),
                ('Marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventario.marca')),
                ('Ram', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventario.ram')),
            ],
            options={
                'verbose_name_plural': 'Laptop',
            },
        ),
        migrations.CreateModel(
            name='Impresora_Scan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Modelo', models.CharField(max_length=40)),
                ('Direccion_Mac', models.CharField(max_length=30, unique=True)),
                ('Observacion', models.CharField(max_length=100)),
                ('Area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventario.area')),
                ('Marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventario.marca')),
            ],
            options={
                'verbose_name_plural': 'Impresora_Scan',
            },
        ),
        migrations.CreateModel(
            name='Elemento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Serial', models.CharField(max_length=15, unique=True)),
                ('Nombre', models.CharField(max_length=30)),
                ('Modelo', models.CharField(max_length=30)),
                ('Observacion', models.TextField(max_length=200)),
                ('Estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventario.estado')),
                ('Marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventario.marca')),
            ],
            options={
                'verbose_name_plural': 'Elemento',
            },
        ),
        migrations.CreateModel(
            name='Dispositivo_de_Red',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Modelo', models.CharField(max_length=40)),
                ('Dispositivo_SSID', models.CharField(max_length=50)),
                ('Ubicacion', models.CharField(max_length=50)),
                ('Fecha_ingreso', models.DateField(blank=True, null=True)),
                ('Direccion_Mac', models.CharField(max_length=30, unique=True)),
                ('Marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventario.marca')),
            ],
            options={
                'verbose_name_plural': 'Dispositivo_de_Red',
            },
        ),
        migrations.AddField(
            model_name='disco_duro',
            name='Marca',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventario.marca'),
        ),
        migrations.CreateModel(
            name='CPU',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Torre', models.CharField(max_length=30)),
                ('Extra', models.CharField(max_length=80)),
                ('MAC', models.CharField(max_length=30, unique=True)),
                ('Acta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventario.acta')),
                ('Disco_Duro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventario.disco_duro')),
                ('Estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventario.estado')),
                ('Licencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventario.licencia')),
                ('Monitor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventario.monitor')),
                ('Motherboard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventario.motherboard')),
                ('Mouse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventario.mouse')),
                ('Procesador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventario.procesador')),
                ('Ram', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventario.ram')),
                ('Teclado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventario.teclado')),
            ],
            options={
                'verbose_name_plural': 'CPU',
            },
        ),
        migrations.CreateModel(
            name='Celular',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Serial', models.CharField(max_length=30, unique=True)),
                ('Modelo', models.CharField(max_length=200)),
                ('Numero_Sim', models.CharField(max_length=30, unique=True)),
                ('IMEI', models.CharField(max_length=30, unique=True)),
                ('IMEI2', models.CharField(max_length=30)),
                ('Mac', models.CharField(max_length=30, unique=True)),
                ('SN_Infraestructura', models.CharField(max_length=50, unique=True)),
                ('Adicional', models.CharField(max_length=200)),
                ('Adicional2', models.CharField(max_length=200)),
                ('Aspecto', models.CharField(max_length=200)),
                ('Cargador', models.CharField(max_length=200)),
                ('Operador', models.CharField(max_length=200)),
                ('Observacion', models.TextField(max_length=200)),
                ('Acta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventario.acta')),
                ('Estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventario.estado')),
                ('Marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventario.marca')),
            ],
            options={
                'verbose_name_plural': 'Celular',
            },
        ),
        migrations.CreateModel(
            name='Asignacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Observacion', models.TextField(max_length=200)),
                ('Acta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventario.acta')),
                ('Cargo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventario.cargo')),
                ('Celular', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventario.celular')),
                ('Laptop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventario.laptop')),
                ('Mouse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventario.mouse')),
                ('Nombres', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventario.persona')),
                ('Periferico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventario.periferico')),
                ('Teclado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventario.teclado')),
                ('Telefono_fijo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventario.telefono_fijo')),
            ],
            options={
                'verbose_name_plural': 'Asignacion',
            },
        ),
    ]
