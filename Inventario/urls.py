from django.urls import include, path
from .views import HomePageView, AboutPageView

from rest_framework import routers
from .views import ActaViewSet, AreaViewSet, AsignacionViewSet,CargoViewSet, CelularViewSet, CPUViewSet, Disco_DuroViewSet, Dispositivo_de_RedViewSet, ElementoViewSet, EstadoViewSet, Impresora_ScanViewSet, LaptopViewSet,LicenciaViewSet, MarcaViewSet, MonitorViewSet, MotherboardViewSet, MouseViewSet, Otros_ElementosViewSet, PersonaViewSet, ProcesadorViewSet, RamViewSet, TabletViewSet, TecladoViewSet, ExtensionViewSet,VoIPViewSet, ModeloRamViewSet, Analista_GestionViewSet, Tarjeta_GraficaViewSet, CargadorViewSet

router = routers.DefaultRouter()
router.register('Acta', ActaViewSet)
router.register('Area', AreaViewSet)
router.register('Asignacion', AsignacionViewSet)
router.register('Analista_Gestion', Analista_GestionViewSet)
router.register('Cargo', CargoViewSet)
router.register('Cargador', CargadorViewSet)
router.register('Celular', CelularViewSet)
router.register('CPU', CPUViewSet)
router.register('Disco_Duro', Disco_DuroViewSet)
router.register('Dispositivo_de_Red', Dispositivo_de_RedViewSet)
router.register('Elemento', ElementoViewSet)
router.register('Estado', EstadoViewSet)
router.register('Impresora_Scan', Impresora_ScanViewSet)
router.register('Laptop', LaptopViewSet)
router.register('Licencia', LicenciaViewSet)
router.register('Marca', MarcaViewSet)
router.register('Monitor', MonitorViewSet)
router.register('Motherboard', MotherboardViewSet)
router.register('Mouse', MouseViewSet)
router.register('Otros_Elementos', Otros_ElementosViewSet)
router.register('Persona', PersonaViewSet)
router.register('Procesador', ProcesadorViewSet)
router.register('Ram', RamViewSet)
router.register('Tablet', TabletViewSet)
router.register('Teclado', TecladoViewSet)
router.register('Extension', ExtensionViewSet)
router.register('VoIP', VoIPViewSet)
router.register('ModeloRam', ModeloRamViewSet)
router.register('Tarjeta_Grafica', Tarjeta_GraficaViewSet)

urlpatterns = [
    #path('home', HomePageView.as_view(), name='home')
    path('api/v1/', include(router.urls)),
    path('about', AboutPageView.as_view(), name='about')]