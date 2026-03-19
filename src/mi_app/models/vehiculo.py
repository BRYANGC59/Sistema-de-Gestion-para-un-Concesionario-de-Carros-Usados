from dataclasses import dataclass
from enum import Enum
from src.mi_app.exceptions import PrecioInvalidoError

class EstadoVehiculo(Enum):
    """Representa los posibles estados de un vehículo en el inventario."""
    DISPONIBLE = "Disponible"
    RESERVADO = "Reservado"
    VENDIDO = "Vendido"

@dataclass
class VehiculoUsado:
    """
    Entidad principal que representa un carro dentro del concesionario.
    Se autovalida al momento de ser instanciada.
    """
    id_vehiculo: int
    marca: str
    modelo: str
    anio: int
    precio: float
    kilometraje: int
    estado: EstadoVehiculo = EstadoVehiculo.DISPONIBLE

    def __post_init__(self) -> None:
        """Ejecuta validaciones automáticas al instanciar el vehículo."""
        self._validar_precio()
        self._validar_kilometraje()

    def _validar_precio(self) -> None:
        """Verifica que el precio no sea un número negativo."""
        if self.precio < 0:
            raise PrecioInvalidoError("El precio no puede ser negativo.")

    def _validar_kilometraje(self) -> None:
        """Verifica que el kilometraje no sea un número negativo."""
        if self.kilometraje < 0:
            raise ValueError("El kilometraje no puede ser negativo.")