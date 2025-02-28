from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from .serializers import (
    MedicoSerializer,
    EspecialidadSerializer,
    MedicoListSerializer,
    ConsultaSerializer,
    ConsultaListSerializer,
)
from .models import Medico, Especialidad, Consulta


class MedicoViewSet(ModelViewSet):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        medicos = Medico.objects.all().filter(agregado_por=self.request.user)

        return Response({"medicos": MedicoListSerializer(medicos, many=True).data})

    def create(self, request, *args, **kwargs):
        request.data["agregado_por"] = self.request.user.id
        medico = Medico.objects.get(
            id=super().create(request, *args, **kwargs).data["id"]
        )

        return Response(data=MedicoListSerializer(medico).data)

    def partial_update(self, request, *args, **kwargs):
        medico = Medico.objects.get(
            id=super().partial_update(request, *args, **kwargs).data["id"]
        )

        return Response(data=MedicoListSerializer(medico).data)


class EspecialidadViewSet(ModelViewSet):
    queryset = Especialidad.objects.all()
    serializer_class = EspecialidadSerializer
    permission_classes = [AllowAny]


class ConsultaViewSet(ModelViewSet):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        consultas = Consulta.objects.all().filter(usuario=self.request.user)

        return Response(
            {"consultas": ConsultaListSerializer(consultas, many=True).data}
        )

    def create(self, request, *args, **kwargs):
        request.data["usuario"] = self.request.user.id
        consulta = Consulta.objects.get(
            id=super().create(request, *args, **kwargs).data["id"]
        )

        return Response(data=ConsultaListSerializer(consulta).data)

    def partial_update(self, request, *args, **kwargs):
        consulta = Consulta.objects.get(
            id=super().partial_update(request, *args, **kwargs).data["id"]
        )

        return Response(data=ConsultaListSerializer(consulta).data)
