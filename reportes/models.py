from django.db import models
from usuarios.models import Usuario
from minio_storage.storage import MinioMediaStorage
import uuid


def generar_nombre(instance, filename):
    """
    Genera un nombre unico para el archivo y lo retorna
    """

    # obtiene la extension del archivo
    extension = filename.split(".")[-1]
    # obtiene el nombre del usuario
    usuario = instance.reporte.usuario.username

    # genera una cadena de caracteres para el nombre del archivo y elimina todos los "-" que tenga
    caracteres = str(uuid.uuid4()).replace("-", "")
    # crea el nuevo nombre
    nuevo_nombre = usuario + "." + caracteres + "." + extension
    # retorna el nuevo nombre
    return "reports/{0}".format(nuevo_nombre)


# Create your models here.
class Reporte(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    data = models.JSONField()


class ReporteFile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    reporte = models.OneToOneField(Reporte, on_delete=models.CASCADE)
    file = models.FileField(upload_to=generar_nombre, storage=MinioMediaStorage())
