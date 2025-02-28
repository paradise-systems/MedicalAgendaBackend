from rest_framework import routers

from .views import (
    UsuarioViewSet,
    ChangeUserProfileViewSet,
    GeneroViewSet,
    TensionViewSet,
)

router = routers.DefaultRouter()

router.register(r"users", UsuarioViewSet, basename="users")
router.register(r"profile", ChangeUserProfileViewSet, basename="profile")
router.register(r"generos", GeneroViewSet, basename="generos")
router.register(r"tensiones", TensionViewSet, basename="tensiones")

urlpatterns = router.urls
