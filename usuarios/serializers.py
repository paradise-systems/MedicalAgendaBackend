from rest_framework import serializers
from .models import Usuario, Genero, Tension


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        exclude = ["is_superuser", "is_staff", "is_active", "last_login", "date_joined"]


class GeneroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genero
        fields = "__all__"


class TensionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tension
        fields = "__all__"


class TensionListSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer(read_only=True)

    class Meta:
        model = Tension
        fields = "__all__"
