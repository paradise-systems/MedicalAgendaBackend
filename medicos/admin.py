from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Medico, Especialidad, Consulta
from unfold.decorators import action
from django.urls import reverse
from django.shortcuts import redirect


class EspecialidadAdmin(ModelAdmin):
    list_display = ("especialidad", "create_at", "update_at")
    list_filter = ("create_at", "update_at")
    search_fields = ("especialidad",)

    actions_row = ["delete_especialidad"]

    @action(description="Eliminar Especialidad", url_path="delete-especialidad")
    def delete_especialidad(self, request, object_id):
        return redirect(reverse("admin:medicos_especialidad_delete", args=[object_id]))


class MedicoAdmin(ModelAdmin):
    list_display = (
        "id",
        "nombre",
        "apellido",
        "telefono",
        "institucion",
        "especialidad",
        "agregado_por",
        "create_at",
        "update_at",
    )
    list_filter = ("create_at", "update_at", "especialidad")
    search_fields = ("nombre", "apellido", "institucion")

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "nombre",
                    "apellido",
                    "foto",
                    "telefono",
                    "institucion",
                    "especialidad",
                    "agregado_por",
                )
            },
        ),
    )

    actions_row = ["delete_medico"]

    @action(description="Eliminar Medico", url_path="delete-medico")
    def delete_medico(self, request, object_id):
        return redirect(reverse("admin:medicos_medico_delete", args=[object_id]))


class ConsultaAdmin(ModelAdmin):
    list_display = ("id", "medico", "usuario", "create_at", "update_at")
    list_filter = ("create_at", "update_at")
    search_fields = ("medico", "usuario")

    fieldsets = (
        (
            None,
            {"fields": ("medico", "usuario", "diagnostico", "tratamiento")},
        ),
    )

    actions_row = ["delete_consulta"]

    @action(description="izar Consulta", url_path="delete-consulta")
    def delete_consulta(self, request, object_id):
        return redirect(reverse("admin:medicos_consulta_delete", args=[object_id]))


admin.site.register(Especialidad, EspecialidadAdmin)
admin.site.register(Medico, MedicoAdmin)
admin.site.register(Consulta, ConsultaAdmin)
