from fastapi import APIRouter, Depends, HTTPException
from typing import List
from api.schemas.vehiculo_schema import VehiculoCreate, VehiculoResponse

#Router específico para vehículos
router = APIRouter(prefix="/vehiculos", tags=["Vehículos"])

@router.get("/", response_model=List[VehiculoResponse])
def obtener_vehiculos():
    pass

@router.post("/", response_model=VehiculoResponse)
def crear_vehiculo(vehiculo: VehiculoCreate):
    pass

@router.put("/{vehiculo_id}", response_model=VehiculoResponse)
def actualizar_vehiculo(vehiculo_id: int, vehiculo: VehiculoCreate):
    pass

@router.delete("/{vehiculo_id}")
def eliminar_vehiculo(vehiculo_id: int):
    pass 