from django.urls import path
from .views import create_report

urlpatterns = [
    path("report/", create_report, name="create-report"),
]
