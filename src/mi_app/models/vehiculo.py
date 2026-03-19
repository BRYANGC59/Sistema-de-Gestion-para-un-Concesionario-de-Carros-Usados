from dataclasses import dataclass
from enum import Enum

class EstadoVehiculo(Enum):
    DISPONIBLE = "Disponible"
    RESERVADO = "Reservado"
    VENDIDO = "Vendido"

@dataclass
class VehiculoUsado:
    id_vehiculo: int
    marca: str
    modelo: str
    anio: int
    precio: float
    kilometraje: int
    estado: EstadoVehiculo = EstadoVehiculo.DISPONIBLE

    def __post_init__(self) -> None:
        self._validar_precio()
        self._validar_kilometraje()

    def _validar_precio(self) -> None:
        if self.precio < 0:
            raise ValueError(f"El precio no puede ser negativo. Valor recibido: {self.precio}")

    def _validar_kilometraje(self) -> None:
        if self.kilometraje < 0:
            raise ValueError(f"El kilometraje no puede ser negativo. Valor recibido: {self.kilometraje}")