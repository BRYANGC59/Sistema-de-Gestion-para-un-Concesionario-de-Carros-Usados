from sqlmodel import SQLModel, Field
from typing import Optional

class Cliente(SQLModel, table=True):
    cedula: int = Field(primary_key=True, description="Número de identificación del cliente")
    nombre: str
    edad: Optional[int] = None
    telefono: str
    correo: Optional[str] = None
    cantidad_negocios: int = Field(default=0, description="Cuántos carros ha comprado/vendido")