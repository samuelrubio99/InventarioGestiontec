from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Marca(models.Model):                  
    Nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.Nombre
    
    class Meta:
        verbose_name_plural = _('Marca')

class Estado(models.Model):                  
    Estado = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.Estado
    
    class Meta:
        verbose_name_plural = _('Estado')
 
class Acta(models.Model):                  
    Tipo = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.Tipo
    
    class Meta:
        verbose_name_plural = _('Acta')        
       
        
class Licencia(models.Model):                  
    Software = models.CharField(max_length=130, null=True)

    def __str__(self):
        return self.Software
    
    class Meta:
        verbose_name_plural = _('Licencia')
        
        
class Motherboard(models.Model):
    Serial = models.CharField(max_length=40, unique=True)
    Marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    Estructura = models.CharField(max_length=200) 
        
    def __str__(self):
        return self.Serial
    
    class Meta:
        verbose_name_plural = _('Motherboard')
        

class ModeloRam(models.Model):
    Modelo = models.CharField(max_length=30)

    def __str__(self):
        return self.Modelo
    
    class Meta:
        verbose_name_plural = _('ModeloRam')
        
class Ram(models.Model):
    Serial = models.CharField(max_length=40, unique=True)
    Modelo = models.ForeignKey(ModeloRam, on_delete=models.CASCADE)
    Marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    Capacidad = models.CharField(max_length=5)
    
    def __str__(self):
        return self.Serial
    
    class Meta:
        verbose_name_plural = _('Ram')

        
class Disco_Duro(models.Model):
    Serial = models.CharField(max_length=15, unique=True)
    Tipo = models.CharField(max_length=5)
    Marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    Capacidad = models.CharField(max_length=5)
    
    def __str__(self):
        return self.Serial
    
    class Meta:
        verbose_name_plural = _('Disco_Duro') 
        
class Tarjeta_Grafica(models.Model):
    Modelo = models.CharField(max_length=40, unique=True)
    Tipo_de_Interfaz = models.CharField(max_length=40)
    
    def __str__(self):
        return self.Modelo  
    
    class Meta:
        verbose_name_plural = _('Tarjeta_Grafica')       
        
    
class Procesador(models.Model):
    Modelo = models.CharField(max_length=100)
    Estructura = models.CharField(max_length=50) 
        
    def __str__(self):
        return self.Modelo
    
    class Meta:
        verbose_name_plural = _('Procesador') 

class Monitor(models.Model):
    Serial = models.CharField(max_length=15, unique=True)
    Modelo = models.CharField(max_length=30)
    Marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    Estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    Observacion = models.TextField(max_length=200)
    
    def __str__(self):
        return self.Modelo
    
    class Meta:
        verbose_name_plural = _('Monitor')
        
        
class Mouse(models.Model):
    Serial = models.CharField(max_length=15, unique=True)
    Estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    Observacion = models.TextField(max_length=200)
    
    def __str__(self):
        return self.Serial
    
    class Meta:
        verbose_name_plural = _('Mouse')
        
        
class Teclado(models.Model):
    Serial = models.CharField(max_length=15, unique=True)
    Modelo = models.CharField(max_length=30)
    Marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    Estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    Observacion = models.TextField(max_length=200)
    
    def __str__(self):
        return self.Modelo
    
    class Meta:
        verbose_name_plural = _('Teclado') 
        
        
      
class Extension(models.Model):
    Serial = models.CharField(max_length=15, unique=True)
    Extension = models.CharField(max_length=30, null=True)
    Direccion_mac = models.CharField(max_length=30)
    Marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    Estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    Observacion = models.TextField(max_length=200)
    
    def __str__(self):
        return self.Extension
    
    class Meta:
        verbose_name_plural = _('Telefono_fijo')
        

class Otros_Elementos(models.Model):
    Serial = models.CharField(max_length=15, unique=True)
    Nombre = models.CharField(max_length=30)
    Marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    Estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    Cantidad = models.IntegerField(blank=True, null=True)
    Observacion = models.TextField(max_length=200)
    
    def __str__(self):
        return self.Nombre   
    
    class Meta:
        verbose_name_plural = _('Otros_Elementos')

class Elemento(models.Model):
    Serial = models.CharField(max_length=15, unique=True)
    Nombre = models.CharField(max_length=30)
    Modelo = models.CharField(max_length=30)
    Marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    Estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    Observacion = models.TextField(max_length=200)
    
    def __str__(self):
        return self.Nombre    
    
    class Meta:
        verbose_name_plural = _('Elemento')

class Area(models.Model):                  
    Area = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return self.Area
    
    class Meta:
        verbose_name_plural = _('Area') 
        
class Cargo(models.Model):                  
    Cargo = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return self.Cargo
    
    class Meta:
        verbose_name_plural = _('Cargo')
                              
class Dispositivo_de_Red(models.Model):                  
    Modelo = models.CharField(max_length=40)
    Dispositivo_SSID = models.CharField(max_length=50)
    Ubicacion = models.CharField(max_length=50)
    Fecha_ingreso = models.DateField(null=True, blank=True)
    Direccion_Mac = models.CharField(max_length=30, unique=True)
    Marca = models.ForeignKey(Marca, on_delete=models.CASCADE)

    def __str__(self):
        return self.Direccion_Mac
    
    class Meta:
        verbose_name_plural = _('Dispositivo_de_Red')  
        
class Impresora_Scan(models.Model):                  
    Modelo = models.CharField(max_length=40)
    Direccion_Mac = models.CharField(max_length=30, unique=True)
    Area = models.ForeignKey(Area, on_delete=models.CASCADE)
    Marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    Observacion = models.CharField(max_length=100)

    def __str__(self):
        return self.Modelo
    
    class Meta:
        verbose_name_plural = _('Impresora_Scan')  
        
class VoIP(models.Model):                  
    Modelo = models.CharField(max_length=40)
    Area = models.ForeignKey(Area, on_delete=models.CASCADE)
    Direccion_IP = models.CharField(max_length=30, unique=True)
    Direccion_Mac = models.CharField(max_length=30, unique=True)
    Extencion_Telefono = models.CharField(max_length=50)
    Observacion = models.CharField(max_length=100)

    def __str__(self):
        return self.Extencion_Telefono
    
    class Meta:
        verbose_name_plural = _('VoIP')  
        
class Cargador(models.Model):
    Modelo = models.CharField(max_length=30)
    Marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    Estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.Modelo
    
    class Meta:
        verbose_name_plural = _('Cargador')

# Create your models here.


class Tablet(models.Model):
    Serial = models.CharField(max_length=30, unique= True)
    Modelo = models.CharField(max_length=200)
    Direccion_Mac = models.CharField(max_length=30, unique=True)
    Version_SO = models.CharField(max_length=30,default="")
    Cargador = models.CharField(max_length=200)
    Marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    Acta = models.ForeignKey(Acta, on_delete=models.CASCADE)
    Estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    Observacion = models.TextField(max_length=200)
    
    
    def __str__(self):
        return self.Modelo
    
    class Meta:
        verbose_name_plural = _('Tablet')
        
class Celular(models.Model):
    Serial = models.CharField(max_length=30, unique= True)
    Modelo = models.CharField(max_length=200)
    Numero_Sim = models.CharField(max_length=30, unique= True)
    IMEI = models.CharField(max_length=30, unique= True)
    IMEI2 = models.CharField(max_length=30)
    Mac = models.CharField(max_length=30, unique=True)
    SN_Infraestructura = models.CharField(max_length=50, unique=True)
    Adicional = models.CharField(max_length=200)
    Adicional2 = models.CharField(max_length=200)
    Aspecto = models.CharField(max_length=200)
    Cargador = models.CharField(max_length=200)
    Marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    Acta = models.ForeignKey(Acta, on_delete=models.CASCADE)
    Operador = models.CharField(max_length=200)
    Estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    Observacion = models.TextField(max_length=200)
    
    
    def __str__(self):
        return self.Modelo
    
    class Meta:
        verbose_name_plural = _('Celular')        

class Persona(models.Model):
    Nombres = models.CharField(max_length=200)
    Apellidos = models.CharField(max_length=200)
    Correo = models.EmailField(max_length=100, unique=True)
    Numero_Celular = models.CharField(max_length=70,default="")
    Area = models.ForeignKey(Area, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.Nombres
    
    class Meta:
        verbose_name_plural = _('Persona')
        
        
class Analista_Gestion(models.Model):
    Nombres = models.CharField(max_length=200)
    Apellidos = models.CharField(max_length=200)
    Correo = models.EmailField(max_length=100, unique=True)
    Numero_Celular = models.CharField(max_length=70,default="")

    def __str__(self):
        return self.Nombres
    
    class Meta:
        verbose_name_plural = _('Analista_Gestion')      

class CPU(models.Model):
    Nombre_Equipo = models.CharField(max_length=80, unique=True, null=True)
    Torre = models.CharField(max_length=30)
    Extra = models.CharField(max_length=80)
    MAC = models.CharField(max_length=30, unique=True)
    Motherboard = models.ForeignKey(Motherboard, on_delete=models.CASCADE)
    Disco_Duro = models.ForeignKey(Disco_Duro, on_delete=models.CASCADE)
    Ram = models.ForeignKey(Ram, on_delete=models.CASCADE)
    Procesador = models.ForeignKey(Procesador, on_delete=models.CASCADE)
    Monitor = models.ForeignKey(Monitor, on_delete=models.CASCADE)
    Teclado = models.ForeignKey(Teclado, on_delete=models.CASCADE)
    Mouse = models.ForeignKey(Mouse, on_delete=models.CASCADE)
    Licencia = models.ForeignKey(Licencia, on_delete=models.CASCADE)
    Estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    Acta = models.ForeignKey(Acta, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.Nombre_Equipo
    
    class Meta:
        verbose_name_plural = _('CPU')
                
class Laptop(models.Model):
    Nombre_Equipo = models.CharField(max_length=80,unique=True, null=True )
    Serial = models.CharField(max_length=30, unique=True)
    Modelo = models.CharField(max_length=80)
    Marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    Disco_Duro = models.ForeignKey(Disco_Duro, on_delete=models.CASCADE)
    Ram = models.ForeignKey(Ram, on_delete=models.CASCADE)
    Tarjeta_Grafica = models.CharField(max_length=80)
    Licencia = models.ForeignKey(Licencia, on_delete=models.CASCADE)
    LAN_MAC = models.CharField(max_length=30, unique=True)
    WLAN_MAC = models.CharField(max_length=30, unique=True)
    Ultimo_Backup = models.DateField(null=True, blank=True)
    Cargador = models.CharField(max_length=80)
    Bateria = models.CharField(max_length=80)
    Estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    Acta = models.ForeignKey(Acta, on_delete=models.CASCADE)
    Observacion = models.TextField(max_length=200)

    def __str__(self):
        return self.Nombre_Equipo
    
    class Meta:
        verbose_name_plural = _('Laptop')
        
class Asignacion(models.Model):
    Nombres = models.ForeignKey(Persona, on_delete=models.CASCADE)
    Cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)
    Laptop = models.ForeignKey(Laptop, on_delete=models.CASCADE)
    Teclado = models.ForeignKey(Teclado, on_delete=models.CASCADE)
    Mouse = models.ForeignKey(Mouse, on_delete=models.CASCADE)
    Celular = models.ForeignKey(Celular, on_delete=models.CASCADE)
    Extencion = models.ForeignKey(Extension, on_delete=models.CASCADE)
    Otro_Elemento = models.ForeignKey(Otros_Elementos, on_delete=models.CASCADE)
    Fecha_Inicio = models.DateField(null=True, blank=True) 
    Fecha_Final = models.DateField(null=True, blank=True)
    Analista_a_Cargo = models.ForeignKey(Analista_Gestion, on_delete=models.CASCADE, null=True)
    Observacion = models.TextField(max_length=200)
    
    class Meta():
        verbose_name_plural = _("Asignacion")
    