# Generated by Django 5.1.1 on 2024-10-30 01:44

import django.db.models.deletion
import examenes.models
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Categoria",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "categoria",
                    models.CharField(
                        max_length=100, unique=True, verbose_name="Categoria"
                    ),
                ),
                (
                    "create_at",
                    models.DateTimeField(
                        auto_now=True, null=True, verbose_name="Fecha de Creacion"
                    ),
                ),
                (
                    "update_at",
                    models.DateTimeField(
                        auto_now_add=True,
                        null=True,
                        verbose_name="Fecha de Actualizacion",
                    ),
                ),
            ],
            options={
                "verbose_name": "Categoria",
                "verbose_name_plural": "Categorias",
            },
        ),
        migrations.CreateModel(
            name="Examen",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("titulo", models.CharField(max_length=250, verbose_name="Titulo")),
                (
                    "archivo",
                    models.FileField(
                        blank=True,
                        null=True,
                        upload_to=examenes.models.Examen.upload_to,
                        verbose_name="Archivo",
                    ),
                ),
                ("descripcion", models.TextField(verbose_name="Descripción")),
                (
                    "create_at",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Fecha de Creacion"
                    ),
                ),
                (
                    "update_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Fecha de Actualizacion"
                    ),
                ),
                (
                    "agregado_por",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Agregado Por",
                    ),
                ),
                (
                    "categoria",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="examenes.categoria",
                        verbose_name="Categoria",
                    ),
                ),
            ],
            options={
                "verbose_name": "Examen",
                "verbose_name_plural": "Examenes",
            },
        ),
    ]
