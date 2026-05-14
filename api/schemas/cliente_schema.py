from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class ClienteBase(BaseModel):
    cedula: int = Field(..., description="Cédula de ciudadanía")
    nombre: str = Field(..., min_length=3)
    edad: Optional[int] = Field(None, ge=18)
    telefono: str
    correo: Optional[EmailStr] = None 

class ClienteCreate(ClienteBase):
    pass

class ClienteResponse(ClienteBase):
    cantidad_negocios: int = 0

    class Config:
        from_attributes = True