from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated


from .models import Usuario, Genero, Tension
from .serializers import (
    UsuarioSerializer,
    GeneroSerializer,
    TensionSerializer,
    TensionListSerializer,
)


class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsAdminUser]


class ChangeUserProfileViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        get_usuario = self.queryset.filter(id=self.request.user.id)
        serialize: UsuarioSerializer = self.get_serializer(get_usuario)
        return Response(serialize.data, status=200)

    def retrieve(self, request, *args, **kwargs):
        get_usuario = self.queryset.filter(id=self.request.user.id)
        serialize: UsuarioSerializer = self.get_serializer(get_usuario)
        return Response(serialize.data, status=200)

    def create(self, request, *args, **kwargs):
        return Response({"error": "Method not allowed"}, status=405)

    def destroy(self, request, *args, **kwargs):
        return Response({"error": "Method not allowed"}, status=405)


class GeneroViewSet(ModelViewSet):
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer


class TensionViewSet(ModelViewSet):
    queryset = Tension.objects.all()
    serializer_class = TensionSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        get_tension = self.queryset.filter(usuario=self.request.user)
        serialize: TensionSerializer = self.get_serializer(get_tension, many=True)
        return Response(serialize.data, status=200)

    def create(self, request, *args, **kwargs):
        request.data["usuario"] = self.request.user.id
        tension = Tension.objects.get(
            id=super().create(request, *args, **kwargs).data["id"]
        )

        return Response(data=TensionListSerializer(tension).data)
