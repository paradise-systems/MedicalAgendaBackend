import uuid

from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from usuarios.models import Usuario, Genero

from django_resized import ResizedImageField
from minio_storage.storage import MinioMediaStorage

def generar_nombre(instance, filename):
    """
    Genera un nombre único para el archivo y lo retorna
    """

    # obtiene la extension del archivo
    extension = filename.split(".")[-1]
    # obtiene el nombre del usuario
    usuario = instance.nombre

    # genera una cadena de caracteres para el nombre del archivo y elimina todos los "-" que tenga
    caracteres = str(uuid.uuid4()).replace("-", "")
    # crea el nuevo nombre
    nuevo_nombre = usuario + "." + caracteres + "." + extension
    # retorna el nuevo nombre
    return "medicos-fotos/{0}".format(nuevo_nombre)


# Create your models here.
class Especialidad(models.Model):
    especialidad = models.CharField(
        max_length=100, unique=True, verbose_name="Especialidad"
    )

    create_at = models.DateTimeField(
        auto_now=True, null=True, blank=True, verbose_name="Fecha de Creación"
    )

    update_at = models.DateTimeField(
        auto_now_add=True, null=True, blank=True, verbose_name="Fecha de Actualización"
    )

    genero = models.ForeignKey(
        Genero,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        unique=False,
        verbose_name="Genero",
        help_text="Indica si la especialidad es para un genero en especifico(lo puede dejar en blanco si es para cualquier genero)",
    )

    class Meta:
        verbose_name = "Especialidad"
        verbose_name_plural = "Especialidades"

    def __str__(self):
        return self.especialidad


class Medico(models.Model):
    nombre = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        unique=False,
        verbose_name="Primer Nombre",
    )

    apellido = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        unique=False,
        verbose_name="Primer Apellido",
    )

    telefono = PhoneNumberField(
        blank=False, null=False, unique=False, verbose_name="Número de Teléfono"
    )

    institucion = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        unique=False,
        verbose_name="Institución",
    )

    especialidad = models.ForeignKey(
        Especialidad,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        unique=False,
        verbose_name="Especialidad",
    )

    agregado_por = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        unique=False,
        verbose_name="Agregado Por",
    )

    id = models.UUIDField(
        default=uuid.uuid4, null=False, blank=False, primary_key=True, verbose_name="ID"
    )

    foto = ResizedImageField(
        upload_to=generar_nombre,
        null=True,
        blank=True,
        verbose_name="Foto de Medico",
        size=[736, 736],
        crop=["middle", "center"],
        db_column="medic_image",
        storage=MinioMediaStorage(),
    )

    create_at = models.DateTimeField(
        auto_now=True, null=False, blank=False, verbose_name="Fecha de Creación"
    )

    update_at = models.DateTimeField(
        auto_now_add=True,
        null=False,
        blank=False,
        verbose_name="Fecha de Actualización",
    )

    class Meta:
        verbose_name = "Medico"
        verbose_name_plural = "Medicos"

    def __str__(self):
        return (
            self.nombre
            + " "
            + self.apellido
            + " - "
            + self.institucion
            + " - "
            + self.especialidad.especialidad
        )


class Consulta(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, blank=False, null=False)

    medico = models.ForeignKey(
        Medico,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        unique=False,
        verbose_name="Medico",
    )

    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        unique=False,
        verbose_name="Usuario",
    )

    diagnostico = models.TextField(
        blank=False, null=False, unique=False, verbose_name="Diagnostico"
    )

    tratamiento = models.TextField(
        blank=False, null=False, unique=False, verbose_name="Tratamiento"
    )

    create_at = models.DateTimeField(
        auto_now=True, null=False, blank=False, verbose_name="Fecha de Creación"
    )

    update_at = models.DateTimeField(
        auto_now_add=True,
        null=False,
        blank=False,
        verbose_name="Fecha de Actualización",
    )

    class Meta:
        verbose_name = "Consulta"
        verbose_name_plural = "Consultas"
