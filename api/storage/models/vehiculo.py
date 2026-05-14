from sqlmodel import SQLModel, Field, Column, String
from typing import Optional
from enum import Enum
from pydantic import field_validator


class EstadoVehiculo(str, Enum):
    DISPONIBLE = "Disponible"
    RESERVADO = "Reservado"
    VENDIDO = "Vendido"


class Vehiculo(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    marca: str
    modelo: str
    anio: int
    kilometraje: int
    precio: int
    color: Optional[str] = None

    estado: EstadoVehiculo = Field(
        default=EstadoVehiculo.DISPONIBLE,
        sa_column=Column(String(20))
    )

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
