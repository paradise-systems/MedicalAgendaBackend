# Generated by Django 5.1.1 on 2024-11-06 07:57

import django.db.models.deletion
import reportes.models
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("reportes", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ReporteFile",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("file", models.FileField(upload_to=reportes.models.generar_nombre)),
                (
                    "reporte",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="reportes.reporte",
                    ),
                ),
            ],
        ),
    ]
