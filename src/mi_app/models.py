from dataclasses import dataclass
from enum import Enum


class EstadoVehiculo(Enum):
    DISPONIBLE = "Disponible"
    RESERVADO = "Reservado"
    VENDIDO = "Vendido"

@dataclass
class Vehiculo:
    id_vehiculo: int
    marca: str
    modelo: str
    ano: int
    precio: float
    kilometraje: int
    estado: EstadoVehiculo = EstadoVehiculo.DISPONIBLE