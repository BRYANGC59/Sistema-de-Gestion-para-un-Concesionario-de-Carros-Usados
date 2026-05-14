from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum

class EstadoVehiculo(str, Enum):
    DISPONIBLE = "Disponible"
    RESERVADO = "Reservado"
    VENDIDO = "Vendido"

class VehiculoBase(BaseModel):
    marca: str
    modelo: str
    anio: int = Field(gt=1990)
    kilometraje: int = Field(ge=0)
    precio: int = Field(gt=0)
    color: Optional[str] = None
    estado: EstadoVehiculo = EstadoVehiculo.DISPONIBLE

class VehiculoCreate(VehiculoBase):
    pass

class VehiculoResponse(VehiculoBase):
    id: int