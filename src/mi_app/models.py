from dataclasses import dataclass

@dataclass
class Vehiculo:
    id_vehiculo: int
    marca: str
    modelo: str
    ano: int
    precio: float
    disponible: bool = True