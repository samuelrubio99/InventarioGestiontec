from django.urls import include, path
from .views import HomePageView, AboutPageView

from rest_framework import routers
from .views import ActaViewSet, AreaViewSet, AsignacionViewSet,CargoViewSet, CelularViewSet, CPUViewSet, Disco_DuroViewSet, Dispositivo_de_RedViewSet, ElementoViewSet, EstadoViewSet, Impresora_ScanViewSet, LaptopViewSet,LicenciaViewSet, MarcaViewSet, MonitorViewSet, MotherboardViewSet, MouseViewSet, PerifericoViewSet, PersonaViewSet, ProcesadorViewSet, RamViewSet, TabletViewSet, TecladoViewSet, Telefono_fijoViewSet,VoIPViewSet

router = routers.DefaultRouter()
router.register('Acta', ActaViewSet)
router.register('Area', AreaViewSet)
router.register('Asignacion', AsignacionViewSet)
router.register('Cargo', CargoViewSet)
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
router.register('Periferico', PerifericoViewSet)
router.register('Persona', PersonaViewSet)
router.register('Procesador', ProcesadorViewSet)
router.register('Ram', RamViewSet)
router.register('Tablet', TabletViewSet)
router.register('Teclado', TecladoViewSet)
router.register('Telefono_fijo', Telefono_fijoViewSet)
router.register('VoIP', VoIPViewSet)

urlpatterns = [
    #path('home', HomePageView.as_view(), name='home')
    path('api/v1/', include(router.urls)),
    path('about', AboutPageView.as_view(), name='about')]