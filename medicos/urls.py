from rest_framework.routers import DefaultRouter

from .views import MedicoViewSet, EspecialidadViewSet, ConsultaViewSet

router = DefaultRouter()

router.register(r"medicos", MedicoViewSet, basename="medicos")
router.register(r"especialidades", EspecialidadViewSet, basename="especialidades")
router.register(r"consultas", ConsultaViewSet, basename="consultas")

urlpatterns = router.urls
