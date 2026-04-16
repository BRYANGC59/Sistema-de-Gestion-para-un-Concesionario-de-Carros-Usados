from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime


class Venta(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    cliente_id: int = Field(foreign_key="cliente.cedula")

    carro_id: int = Field(foreign_key="vehiculo.id", unique=True)

    fecha: datetime = Field(default_factory=datetime.now)
    precio_final: int