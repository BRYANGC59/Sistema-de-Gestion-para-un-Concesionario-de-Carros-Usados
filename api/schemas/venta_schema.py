from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class VentaBase(BaseModel):
    cliente_id: int
    carro_id: int
    precio_final: int = Field(..., gt=0)

class VentaCreate(VentaBase):
    pass

class VentaResponse(VentaBase):
    id: int
    fecha: datetime

    class Config:
        from_attributes = True