from rest_framework import serializers
from .models import Reporte, ReporteFile


class ReporteSerializer(serializers.ModelSerializer):
    data = serializers.JSONField()

    class Meta:
        model = Reporte
        fields = "__all__"

    def validate_data(self, value):
        if type(value) != list:
            raise serializers.ValidationError(
                "la data debe ser una lista de diccionarios/objetos"
            )
        if len(value) == 0:
            raise serializers.ValidationError("la data no puede estar vacía")
        if type(value[0]) != dict:
            raise serializers.ValidationError(
                "la data debe ser una lista de diccionarios/objetos"
            )

        return value


class ReporteFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReporteFile
        fields = "__all__"
