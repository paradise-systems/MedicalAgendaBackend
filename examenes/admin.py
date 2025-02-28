from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Examen, Categoria
from unfold.decorators import action
from django.urls import reverse
from django.shortcuts import redirect


# Register your models here.
class CategoriaAdmin(ModelAdmin):
    list_display = ("id", "categoria", "create_at", "update_at")
    list_filter = ("create_at", "update_at")

    actions_row = ["delete_categoria"]
    search_fields = ("categoria",)

    @action(description="Eliminar Categoria", url_path="delete-categoria")
    def delete_categoria(self, request, object_id):
        return redirect(reverse("admin:examenes_categoria_delete", args=[object_id]))


class ExamenAdmin(ModelAdmin):
    list_display = (
        "id",
        "titulo",
        "archivo",
        "categoria",
        "agregado_por",
        "create_at",
        "update_at",
    )
    list_filter = ("create_at", "update_at", "categoria")

    search_fields = ("categoria", "agregado_por")

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "titulo",
                    "categoria",
                    "agregado_por",
                    "archivo",
                    "descripcion",
                )
            },
        ),
    )

    actions_row = ["delete_examen"]

    @action(description="Eliminar Examen", url_path="delete-examen")
    def delete_examen(self, request, object_id):
        return redirect(reverse("admin:examenes_examen_delete", args=[object_id]))


admin.site.register(Examen, ExamenAdmin)
admin.site.register(Categoria, CategoriaAdmin)
