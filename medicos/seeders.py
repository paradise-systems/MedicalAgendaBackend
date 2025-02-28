import pathlib

from django_seeding import seeders
from django_seeding.seeder_registry import SeederRegistry
from .models import Especialidad
from core.settings import BASE_DIR


@SeederRegistry.register
class EspecialidadSeeder(seeders.CSVFileModelSeeder):
    model = Especialidad
    csv_file_path = str(
        pathlib.Path(BASE_DIR / "medicos" / "data" / "especialidades.csv")
    )
