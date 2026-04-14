from typing import Optional

from sqlmodel import SQLModel, Field, Session, create_engine, select
from pydantic import field_validator
from enum import Enum
from src.mi_app.exceptions import PrecioInvalidoError


class EstadoVehiculo(Enum):
    """Representa los posibles estados de un vehículo en el inventario."""
    DISPONIBLE = "Disponible"
    RESERVADO = "Reservado"
    VENDIDO = "Vendido"


class Vehiculo(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    marca: str = Field(index=True)
    modelo: str
    anio: int
    kilometraje: int
    precio: int
    color: Optional[str] = None
    estado: EstadoVehiculo = Field(default=EstadoVehiculo.DISPONIBLE)

    @field_validator("precio")
    @classmethod
    def validar_precio(cls, value: int) -> int:
        if value < 0:
            raise PrecioInvalidoError("El precio no puede ser negativo.")
        return value

    @field_validator("kilometraje")
    @classmethod
    def validar_kilometraje(cls, value: int) -> int:
        if value < 0:
            raise ValueError("El kilometraje no puede ser negativo.")
        return value
