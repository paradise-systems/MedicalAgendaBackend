import uuid

from django.db import models

from usuarios.models import Usuario

from minio_storage.storage import MinioMediaStorage

# Create your models here.
class Categoria(models.Model):
    categoria = models.CharField(max_length=100, unique=True, verbose_name="Categoria")

    create_at = models.DateTimeField(
        auto_now=True, null=True, blank=True, verbose_name="Fecha de Creacion"
    )

    update_at = models.DateTimeField(
        auto_now_add=True, null=True, blank=True, verbose_name="Fecha de Actualizacion"
    )

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.categoria


class Examen(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, null=False, blank=False, primary_key=True, verbose_name="ID"
    )

    def upload_to(instance, filename):
        # obtiene la extension del archivo
        extension: str = filename.split(".")[-1]

        # obtiene el nombre del usuario

        usuario = instance.agregado_por.username

        # genera una cadena de caracteres para el nombre del archivo y elimina todos los "-" que tenga
        caracteres = str(uuid.uuid4()).replace("-", "")

        # crea el nuevo nombre
        nuevo_nombre = usuario + "." + caracteres + "." + extension

        # crea el nuevo nombre y reemplaza todos los espacios por "-"
        nuevo_nombre = str(usuario + "." + caracteres + "." + extension).replace(
            " ", "-"
        )

        # retorna el nuevo nombre
        return "examenes/{0}/{1}/{2}".format(usuario, extension.upper(), nuevo_nombre)

    titulo = models.CharField(
        max_length=250, blank=False, null=False, unique=False, verbose_name="Titulo"
    )

    archivo = models.FileField(
        upload_to=upload_to,
        blank=True,
        null=True,
        unique=False,
        verbose_name="Archivo",
        storage=MinioMediaStorage(),
    )

    descripcion = models.TextField(
        blank=False,
        null=False,
        unique=False,
        verbose_name="Descripción",
    )

    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        unique=False,
        verbose_name="Categoria",
    )

    agregado_por = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        unique=False,
        verbose_name="Agregado Por",
    )

    create_at = models.DateTimeField(
        auto_now=True, null=False, blank=False, verbose_name="Fecha de Creacion"
    )

    update_at = models.DateTimeField(
        auto_now_add=True,
        null=False,
        blank=False,
        verbose_name="Fecha de Actualizacion",
    )

    class Meta:
        verbose_name = "Examen"
        verbose_name_plural = "Examenes"

    def __str__(self):
        return (
            self.categoria.categoria
            + " - "
            + self.agregado_por.username
            + " - "
            + str(self.create_at)
        )
