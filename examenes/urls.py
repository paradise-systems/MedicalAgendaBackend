from rest_framework.routers import DefaultRouter

from .views import ExamenViewSet, CategoriaViewSet

router = DefaultRouter()

router.register(r"examenes", ExamenViewSet, basename="medicos")
router.register(r"categorias", CategoriaViewSet, basename="especialidades")

urlpatterns = router.urls
