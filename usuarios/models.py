import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django_resized import ResizedImageField
from phonenumber_field.modelfields import PhoneNumberField
from minio_storage.storage import MinioMediaStorage

def generar_nombre(instance, filename):
    """
    Genera un nombre unico para el archivo y lo retorna
    """

    # obtiene la extension del archivo
    extension = filename.split(".")[-1]
    # obtiene el nombre del usuario
    usuario = instance.username

    # genera una cadena de caracteres para el nombre del archivo y elimina todos los "-" que tenga
    caracteres = str(uuid.uuid4()).replace("-", "")
    # crea el nuevo nombre
    nuevo_nombre = usuario + "." + caracteres + "." + extension
    # retorna el nuevo nombre
    return "avatars/{0}".format(nuevo_nombre)


def generar_strings():
    return "no-content." + (str(uuid.uuid4()).replace("-", ""))


class Genero(models.Model):
    genero = models.CharField(max_length=40, unique=True, verbose_name="Genero")
    create_at = models.DateTimeField(
        auto_now=True, null=False, blank=False, verbose_name="Fecha de Creación"
    )
    update_at = models.DateTimeField(
        auto_now_add=True,
        null=False,
        blank=False,
        verbose_name="Fecha de Actualización",
    )

    def __str__(self):
        return self.genero


class Usuario(AbstractUser):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, blank=False, null=False)

    ci = models.IntegerField(
        unique=True, blank=True, null=True, verbose_name="Cédula de Identidad"
    )

    first_name = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Primer Nombre"
    )

    last_name = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Primer Apellido"
    )

    email = models.EmailField(
        blank=True,
        null=True,
        verbose_name="Correo Electrónico",
        unique=True,
        default=f"no-email.{str(uuid.uuid4()).replace('-', '')}@noemail.com",
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

    avatar = ResizedImageField(
        upload_to=generar_nombre,
        null=True,
        blank=True,
        verbose_name="Avatar",
        size=[736, 736],
        crop=["middle", "center"],
        db_column="profile_image",
        storage=MinioMediaStorage(),
        
    )

    telefono = PhoneNumberField(
        blank=False, null=False, unique=True, verbose_name="Contacto de Emergencia"
    )

    patologia = models.CharField(
        max_length=255, blank=True, null=True, unique=False, verbose_name="Patología"
    )

    genero = models.ForeignKey(
        Genero,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        unique=False,
        verbose_name="Genero",
    )

    alergias = models.CharField(
        max_length=255, blank=True, null=True, unique=False, verbose_name="Alergias"
    )


class Tension(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, blank=False, null=False)

    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        unique=False,
        verbose_name="Usuario",
    )

    sistolic = models.IntegerField(
        blank=False, null=False, unique=False, verbose_name="Sistólica"
    )

    diastolic = models.IntegerField(
        blank=False, null=False, unique=False, verbose_name="Diastólica"
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
