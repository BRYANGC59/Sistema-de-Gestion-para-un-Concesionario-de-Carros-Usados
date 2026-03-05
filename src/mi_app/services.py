from typing import List
from src.mi_app.models import VehiculoUsado
from src.mi_app.storage import cargar_datos, guardar_datos
from src.mi_app.exceptions import VehiculoNoEncontradoError


class InventarioService:
    def _init_(self):
        self._datos_crudos = cargar_datos()
        self.vehiculos = [VehiculoUsado(**v) for v in self._datos_crudos]

    def listar_disponibles(self) -> List[VehiculoUsado]:
        return [v for v in self.vehiculos if v.disponible]

    def buscar_por_id(self, id_vehiculo: int) -> VehiculoUsado:
        for v in self.vehiculos:
            if v.id_vehiculo == id_vehiculo:
                return v
        raise VehiculoNoEncontradoError(f"El vehículo con ID {id_vehiculo} no existe en el lote.")
