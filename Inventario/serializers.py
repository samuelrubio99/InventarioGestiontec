from rest_framework import serializers

from .models import Acta, Area, Asignacion,Cargo, Celular, CPU, Disco_Duro, Dispositivo_de_Red, Elemento, Estado, Impresora_Scan, Laptop,Licencia, Marca, Monitor, Motherboard, Mouse, Periferico, Persona, Procesador, Ram, Tablet, Teclado, Telefono_fijo,VoIP 


class ActaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Acta
        fields = ('Tipo',)
        
class AreaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Area
        fields = ('Area',)


class AsignacionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Asignacion
        fields = ('Nombres','Cargo','Laptop','Teclado','Mouse','Celular','Telefono_fijo','Periferico','Acta','Observacion')


class CargoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cargo
        fields = ('Cargo',)
        
        
class CelularSerializer(serializers.ModelSerializer):

    class Meta:
        model = Celular
        fields = ('Serial','Modelo','Numero_Sim','IMEI','IMEI2','Mac','SN_Infraestructura','Adicional','Adicional2','Aspecto','Cargador','Marca','Acta','Operador','Estado','Observacion')
        
        
class CPUSerializer(serializers.ModelSerializer):

    class Meta:
        model = CPU
        fields = ('Torre','Extra','MAC','Motherboard','Disco_Duro','Ram','Procesador', 'Monitor','Teclado','Mouse','Licencia', 'Estado', 'Acta')
        
class Disco_DuroSerializer(serializers.ModelSerializer):

    class Meta:
        model = Disco_Duro
        fields = ('Serial','Tipo','Marca','Capacidad')
        
        
class Dispositivo_de_RedSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dispositivo_de_Red
        fields = ('Modelo', 'Dispositivo_SSID', 'Ubicacion', 'Fecha_ingreso','Direccion_Mac', 'Marca')
        
class ElementoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Elemento
        fields = ('Serial','Nombre','Modelo', 'Marca', 'Estado', 'Observacion')
        
class EstadoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Estado
        fields = ('Estado',)
        
class Impresora_ScanSerializer(serializers.ModelSerializer):

    class Meta:
        model = Impresora_Scan
        fields = ('Modelo','Direccion_Mac','Area','Marca','Observacion')
        
class LaptopSerializer(serializers.ModelSerializer):

    class Meta:
        model = Laptop
        fields = ('Serial','Modelo','Marca','Disco_Duro','Ram','Tarjeta_Grafica','Licencia','LAN_MAC','WLAN_MAC','Backup','Cargador','Bateria','Estado','Acta','Observacion')
        
class LicenciaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Licencia
        fields = ('modelo',)
        
class MarcaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Marca
        fields = ('Nombre',)
        
class MonitorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Monitor
        fields = ('Serial','Modelo','Marca','Estado','Observacion')
        
class MotherboardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Motherboard
        fields = ('Serial','Marca','Estructura')
        
class MouseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mouse
        fields = ('Serial','Estado','Observacion')
        
class PerifericoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Periferico
        fields = ('Serial','Modelo','Marca','Estado','Cantidad','Observacion')
        
        
class PersonaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Persona
        fields = ('Nombres','Apellidos','Correo','Numero_Celular','Area')
        
        
class ProcesadorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Procesador
        fields = ('Modelo','Estructura')
        
class RamSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ram
        fields = ('Serial','Modelo','Marca','Capacidad')
        
class TabletSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tablet
        fields = ('Serial','Modelo','Direccion_Mac','Version_SO','Cargador','Marca','Acta','Estado','Observacion')
        
class TecladoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teclado
        fields = ('Serial','Modelo','Marca','Estado','Observacion')
        
class Telefono_fijoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Telefono_fijo
        fields = ('Serial','Modelo','Direccion_mac','Marca','Estado','Observacion')
        
class VoIPSerializer(serializers.ModelSerializer):

    class Meta:
        model = VoIP
        fields = ('Modelo','Area','Direccion_IP','Direccion_Mac','Extencion_Telefono','Observacion')