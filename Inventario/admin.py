from django.contrib import admin
from .models import Acta, Area, Asignacion,Cargo, Celular, CPU, Disco_Duro, Dispositivo_de_Red, Elemento, Estado, Impresora_Scan, Laptop,Licencia, Marca, Monitor, Motherboard, Mouse, Otros_Elementos, Persona, Procesador, Ram, Tablet, Teclado, Extension,VoIP, ModeloRam, Analista_Gestion, Tarjeta_Grafica, Cargador

class MarcaAdmin(admin.ModelAdmin):
    list = ('Nombre')
    
class EstadoAdmin(admin.ModelAdmin):
    list = ('Estado')
    
class ActaAdmin(admin.ModelAdmin):
    list = ('Tipo')
    
class LicenciaAdmin(admin.ModelAdmin):
    list = ('modelo')
    
class MotherboardAdmin(admin.ModelAdmin):
    list_display = ('Serial', 'Marca', 'Estructura')
    
class RamAdmin(admin.ModelAdmin):
    list_display = ('Serial', 'Modelo', 'Marca', 'Capacidad')
    
class Disco_DuroAdmin(admin.ModelAdmin):
    list_display = ('Serial', 'Tipo', 'Marca', 'Capacidad')
    
class Tarjeta_GraficaAdmin(admin.ModelAdmin):
    list_display = ('Modelo', 'Tipo_de_Interfaz')
    
class ProcesadorAdmin(admin.ModelAdmin):
    list_display = ('Modelo', 'Estructura')
    
class MonitorAdmin(admin.ModelAdmin):
    list_display = ('Serial', 'Modelo', 'Marca', 'Estado', 'Observacion')

class MouseAdmin(admin.ModelAdmin):
    list_display = ('Serial', 'Estado', 'Observacion')
    
class TecladoAdmin(admin.ModelAdmin):
    list_display = ('Serial', 'Modelo', 'Marca', 'Estado', 'Observacion')
    
class ExtensionAdmin(admin.ModelAdmin):
    list_display = ('Serial', 'Extension', 'Direccion_mac', 'Marca', 'Estado', 'Observacion')
    
class Otros_ElementosAdmin(admin.ModelAdmin):
    list_display = ('Serial', 'Nombre', 'Marca', 'Estado', 'Cantidad',  'Observacion')
    
class ElementoAdmin(admin.ModelAdmin):
    list_display = ('Serial', 'Nombre', 'Modelo', 'Marca', 'Estado', 'Observacion')
    
class AreaAdmin(admin.ModelAdmin):
    list = ('Area')
    
class CargoAdmin(admin.ModelAdmin):
    list = ('Cargo')

class CargadorAdmin(admin.ModelAdmin):
    list = ('Cargador')
    
class Dispositivo_de_RedAdmin(admin.ModelAdmin):
    list_display = ('Modelo', 'Dispositivo_SSID', 'Ubicacion', 'Fecha_ingreso', 'Direccion_Mac', 'Marca')
    
class Impresora_ScanAdmin(admin.ModelAdmin):
    list_display = ('Modelo', 'Direccion_Mac', 'Area', 'Marca', 'Observacion')
    
class VoIPAdmin(admin.ModelAdmin):
    list_display = ('Modelo', 'Direccion_IP', 'Direccion_Mac', 'Extencion_Telefono', 'Observacion')
    
class TabletAdmin(admin.ModelAdmin):
    list_display = ('Serial', 'Modelo', 'Direccion_Mac', 'Version_SO', 'Cargador', 'Marca', 'Acta', 'Estado', 'Observacion')
    
class CelularAdmin(admin.ModelAdmin):
    list_display = ('Serial', 'Modelo', 'Numero_Sim', 'IMEI', 'IMEI2', 'Mac', 'SN_Infraestructura', 'Adicional', 'Adicional2', 'Aspecto', 'Cargador', 'Marca', 'Acta', 'Operador', 'Estado', 'Observacion')
    
class PersonaAdmin(admin.ModelAdmin):
    list_display = ('Nombres','Apellidos','Correo','Numero_Celular', 'Area')
    
class Analista_GestionAdmin(admin.ModelAdmin):
    list_display = ('Nombres','Apellidos','Correo','Numero_Celular')

class CPUAdmin(admin.ModelAdmin):
    list_display = ('Nombre_Equipo','Torre', 'Extra', 'MAC', 'Motherboard', 'Disco_Duro', 'Ram', 'Procesador', 'Monitor', 'Teclado', 'Mouse', 'Licencia', 'Estado', 'Acta')

class LaptopAdmin(admin.ModelAdmin):
    list_display = ('Nombre_Equipo','Serial', 'Modelo', 'Marca', 'Disco_Duro', 'Ram', 'Tarjeta_Grafica', 'Licencia', 'LAN_MAC', 'WLAN_MAC', 'Ultimo_Backup', 'Cargador', 'Bateria', 'Estado', 'Observacion')

class AsignacionAdmin(admin.ModelAdmin):
    list_display = ('Nombres','Cargo','Laptop','Teclado', 'Mouse', 'Celular', 'Extencion', 'Otro_Elemento', 'Fecha_Inicio', 'Fecha_Final', 'Analista_a_Cargo', 'Observacion')

class ModeloRamAdmin(admin.ModelAdmin):
    list_display = ('Modelo',)


admin.site.register(Acta, ActaAdmin)
admin.site.register(Area, AreaAdmin)
admin.site.register(Asignacion, AsignacionAdmin)
admin.site.register(Analista_Gestion, Analista_GestionAdmin)
admin.site.register(Cargo, CargoAdmin)
admin.site.register(Cargador, CargadorAdmin)
admin.site.register(Celular, CelularAdmin)
admin.site.register(CPU, CPUAdmin)
admin.site.register(Disco_Duro, Disco_DuroAdmin)
admin.site.register(Dispositivo_de_Red, Dispositivo_de_RedAdmin)
admin.site.register(Elemento, ElementoAdmin)
admin.site.register(Estado, EstadoAdmin)
admin.site.register(Impresora_Scan, Impresora_ScanAdmin)
admin.site.register(Laptop, LaptopAdmin)
admin.site.register(Licencia, LicenciaAdmin)
admin.site.register(Marca, MarcaAdmin)
admin.site.register(Monitor, MonitorAdmin)
admin.site.register(Motherboard, MotherboardAdmin)
admin.site.register(Mouse, MouseAdmin)
admin.site.register(ModeloRam, ModeloRamAdmin)
admin.site.register(Otros_Elementos, Otros_ElementosAdmin)
admin.site.register(Persona, PersonaAdmin)
admin.site.register(Procesador, ProcesadorAdmin)
admin.site.register(Ram, RamAdmin)
admin.site.register(Tablet, TabletAdmin)
admin.site.register(Teclado, TecladoAdmin)
admin.site.register(Tarjeta_Grafica, Tarjeta_GraficaAdmin)
admin.site.register(Extension, ExtensionAdmin)
admin.site.register(VoIP, VoIPAdmin)


# Register your models here.
