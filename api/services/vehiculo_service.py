from api.storage.repositories.vehiculo_repo import VehiculoRepository
from api.storage.models.vehiculo import Vehiculo
from api.schemas.vehiculo_schema import VehiculoCreate

class VehiculoService:
    def __init__(self, repository: VehiculoRepository):
        self.repo = repository

    def listar_todo(self):
        return self.repo.get_all()

    def crear_nuevo(self, datos: VehiculoCreate):
        nuevo_vehiculo = Vehiculo(**datos.model_dump())
        return self.repo.create(nuevo_vehiculo)