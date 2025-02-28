"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.routers import DefaultRouter

from usuarios.urls import router as usuarios_router
from customAuth.urls import urlpatterns as auth_urls
from examenes.urls import router as examenes_router
from medicos.urls import router as medicos_router
from reportes.urls import urlpatterns as reportes_router
from .views import CSRFAPIView

root_router = DefaultRouter()
root_router.registry.extend(usuarios_router.registry)
root_router.registry.extend(examenes_router.registry)
root_router.registry.extend(medicos_router.registry)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(root_router.urls)),
    path("reports/", include(reportes_router)),
    path("auth/", include(auth_urls)),
    path("csrf/", CSRFAPIView.as_view(), name="csrf"),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
