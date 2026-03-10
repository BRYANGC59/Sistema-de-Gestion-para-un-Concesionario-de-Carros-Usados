from dataclasses import dataclass
from enum import Enum


class EstadoVehiculo(Enum):
    DISPONIBLE = "Disponible"
    RESERVADO = "Reservado"
    VENDIDO = "Vendida"

@dataclass
class VehiculoUsado:
    id_vehiculo: int
    marca: str
    modelo: str
    anio: int
    precio: float
    kilometraje: int
    estado: EstadoVehiculo = EstadoVehiculo.DISPONIBLE