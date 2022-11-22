from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Acta, Area, Asignacion,Cargo, Celular, CPU, Disco_Duro, Dispositivo_de_Red, Elemento, Estado, Impresora_Scan, Laptop,Licencia, Marca, Monitor, Motherboard, Mouse, Otros_Elementos, Persona, Procesador, Ram, Tablet, Teclado, Extension,VoIP, ModeloRam, Analista_Gestion, Tarjeta_Grafica, Cargador
from rest_framework import viewsets
from .serializers import ActaSerializer, AreaSerializer, AsignacionSerializer,CargoSerializer, CelularSerializer, CPUSerializer, Disco_DuroSerializer, Dispositivo_de_RedSerializer, ElementoSerializer, EstadoSerializer, Impresora_ScanSerializer, LaptopSerializer,LicenciaSerializer, MarcaSerializer, MonitorSerializer, MotherboardSerializer, MouseSerializer, Otros_ElementosSerializer, PersonaSerializer, ProcesadorSerializer, RamSerializer, TabletSerializer, TecladoSerializer, ExtensionSerializer,VoIPSerializer, ModeloRamSerializer, Analista_GestionSerializer, Tarjeta_GraficaSerializer, CargadorSerializer

from django.views.decorators.csrf import csrf_exempt
#from rest_framework.decorators import api_view
#from rest_framework.status import (
#    HTTP_400_BAD_REQUEST,
#    HTTP_404_NOT_FOUND,
#    HTTP_200_OK)
#from rest_framework.response import Response

# Create your views here.
class HomePageView(TemplateView): 
    template_name = 'home.html'

class AboutPageView(TemplateView): 
    template_name = 'about.html'
    
class ActaViewSet(viewsets.ModelViewSet):
    queryset = Acta.objects.all()
    serializer_class = ActaSerializer


class AreaViewSet(viewsets.ModelViewSet):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer

class AsignacionViewSet(viewsets.ModelViewSet):
    queryset = Asignacion.objects.all()
    serializer_class = AsignacionSerializer


class CargoViewSet(viewsets.ModelViewSet):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer

class CargadorViewSet(viewsets.ModelViewSet):
    queryset = Cargador.objects.all()
    serializer_class = CargadorSerializer
# Create your views here.

class CelularViewSet(viewsets.ModelViewSet):
    queryset = Celular.objects.all()
    serializer_class = CelularSerializer
    
class CPUViewSet(viewsets.ModelViewSet):
    queryset = CPU.objects.all()
    serializer_class = CPUSerializer
    
class Disco_DuroViewSet(viewsets.ModelViewSet):
    queryset = Disco_Duro.objects.all()
    serializer_class = Disco_DuroSerializer
    
class Dispositivo_de_RedViewSet(viewsets.ModelViewSet):
    queryset = Dispositivo_de_Red.objects.all()
    serializer_class = Dispositivo_de_RedSerializer
    
class ElementoViewSet(viewsets.ModelViewSet):
    queryset = Elemento.objects.all()
    serializer_class = ElementoSerializer
    
class EstadoViewSet(viewsets.ModelViewSet):
    queryset = Estado.objects.all()
    serializer_class = EstadoSerializer
    
class Impresora_ScanViewSet(viewsets.ModelViewSet):
    queryset = Impresora_Scan.objects.all()
    serializer_class = Impresora_ScanSerializer
    
class LaptopViewSet(viewsets.ModelViewSet):
    queryset = Laptop.objects.all()
    serializer_class = LaptopSerializer
    
class LicenciaViewSet(viewsets.ModelViewSet):
    queryset = Licencia.objects.all()
    serializer_class = LicenciaSerializer
    
class MarcaViewSet(viewsets.ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer
    
class MonitorViewSet(viewsets.ModelViewSet):
    queryset = Monitor.objects.all()
    serializer_class = MonitorSerializer
    
class MotherboardViewSet(viewsets.ModelViewSet):
    queryset = Motherboard.objects.all()
    serializer_class = MotherboardSerializer
        
class MouseViewSet(viewsets.ModelViewSet):
    queryset = Mouse.objects.all()
    serializer_class = MouseSerializer
    
class Otros_ElementosViewSet(viewsets.ModelViewSet):
    queryset = Otros_Elementos.objects.all()
    serializer_class = Otros_ElementosSerializer
    
class PersonaViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer
    
class Analista_GestionViewSet(viewsets.ModelViewSet):
    queryset = Analista_Gestion.objects.all()
    serializer_class = Analista_GestionSerializer
    
class ProcesadorViewSet(viewsets.ModelViewSet):
    queryset = Procesador.objects.all()
    serializer_class = ProcesadorSerializer
    
class RamViewSet(viewsets.ModelViewSet):
    queryset = Ram.objects.all()
    serializer_class = RamSerializer
    
class TabletViewSet(viewsets.ModelViewSet):
    queryset = Tablet.objects.all()
    serializer_class = TabletSerializer
    
class TecladoViewSet(viewsets.ModelViewSet):
    queryset = Teclado.objects.all()
    serializer_class = TecladoSerializer
    
class Tarjeta_GraficaViewSet(viewsets.ModelViewSet):
    queryset = Tarjeta_Grafica.objects.all()
    serializer_class = Tarjeta_GraficaSerializer
    
class ExtensionViewSet(viewsets.ModelViewSet):
    queryset = Extension.objects.all()
    serializer_class = ExtensionSerializer
    
class VoIPViewSet(viewsets.ModelViewSet):
    queryset = VoIP.objects.all()
    serializer_class = VoIPSerializer
    
    
class ModeloRamViewSet(viewsets.ModelViewSet):
    queryset = ModeloRam.objects.all()
    serializer_class = ModeloRamSerializer