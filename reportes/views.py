from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.core.files.base import ContentFile

from .serializers import ReporteSerializer, ReporteFileSerializer

import pandas as pd


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_report(request, *args, **kwargs):
    request.data["usuario"] = request.user.id
    serializer = ReporteSerializer(data=request.data)

    if serializer.is_valid():
        reporte = serializer.save()
        dataframe = pd.DataFrame(reporte.data)
        dataframe.to_excel("reporte.xlsx", index=False)

        with open("reporte.xlsx", "rb") as file:
            file_data = ContentFile(file.read(), name="reporte.xlsx")

        reporteFile = ReporteFileSerializer(
            data={"reporte": reporte.id, "file": file_data}
        )

        if reporteFile.is_valid():
            reporteFile.save()
            return Response(reporteFile.data, status=201)

        return Response(data={"error": reporteFile.errors}, status=400)

    return Response(serializer.errors, status=400)
