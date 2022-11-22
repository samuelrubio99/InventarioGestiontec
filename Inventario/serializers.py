from rest_framework import serializers

from .models import Acta, Area, Asignacion,Cargo, Celular, CPU, Disco_Duro, Dispositivo_de_Red, Elemento, Estado, Impresora_Scan, Laptop,Licencia, Marca, Monitor, Motherboard, Mouse, Persona, Procesador, Ram, Tablet, Teclado, Extension,VoIP, ModeloRam, Analista_Gestion, Otros_Elementos, Tarjeta_Grafica, Cargador


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
        fields = ('Nombres','Cargo','Laptop','Teclado','Mouse','Celular','Extencion','Otro_Elemento','Fecha_Inicio', 'Fecha_Final', 'Analista_a_Cargo','Observacion')


class CargoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cargo
        fields = ('Cargo',)
           
class CargadorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cargador
        fields = ('Modelo','Marca', 'Estado')
class CelularSerializer(serializers.ModelSerializer):

    class Meta:
        model = Celular
        fields = ('Serial','Modelo','Numero_Sim','IMEI','IMEI2','Mac','SN_Infraestructura','Adicional','Adicional2','Aspecto','Cargador','Marca','Acta','Operador','Estado','Observacion')
        
        
class CPUSerializer(serializers.ModelSerializer):

    class Meta:
        model = CPU
        fields = ('Nombre_Equipo','Torre','Extra','MAC','Motherboard','Disco_Duro','Ram','Procesador', 'Monitor','Teclado','Mouse','Licencia', 'Estado', 'Acta')
        
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
        fields = ('Nombre_Equipo','Serial','Modelo','Marca','Disco_Duro','Ram','Tarjeta_Grafica','Licencia','LAN_MAC','WLAN_MAC','Ultimo_Backup','Cargador','Bateria','Estado','Acta','Observacion')
        
class LicenciaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Licencia
        fields = ('Software',)
        
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
        
class ModeloRamSerializer(serializers.ModelSerializer):

    class Meta:
        model = ModeloRam
        fields = ('Modelo',)
        
class Otros_ElementosSerializer(serializers.ModelSerializer):

    class Meta:
        model = Otros_Elementos
        fields = ('Serial','Nombre','Marca','Estado','Cantidad','Observacion')
        
        
class PersonaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Persona
        fields = ('Nombres','Apellidos','Correo','Numero_Celular','Area')
        
        
class Analista_GestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Analista_Gestion
        fields = ('Nombres','Apellidos','Correo','Numero_Celular')
        
        
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
        

class Tarjeta_GraficaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tarjeta_Grafica
        fields = ('Modelo','Tipo_de_Interfaz')
        
class ExtensionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Extension
        fields = ('Serial','Extension','Direccion_mac','Marca','Estado','Observacion')
        
class VoIPSerializer(serializers.ModelSerializer):

    class Meta:
        model = VoIP
        fields = ('Modelo','Area','Direccion_IP','Direccion_Mac','Extencion_Telefono','Observacion')
        
        
        
