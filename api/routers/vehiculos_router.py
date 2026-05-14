from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from typing import List

from api.storage.database import get_session
from api.storage.repositories.vehiculo_repo import VehiculoRepository
from api.services.vehiculo_service import VehiculoService
from api.schemas.vehiculo_schema import VehiculoCreate, VehiculoResponse

router = APIRouter(prefix="/vehiculos", tags=["Vehículos"])

# Dependencia para obtener el servicio configurado
def get_vehiculo_service(session: Session = Depends(get_session)):
    repo = VehiculoRepository(session)
    return VehiculoService(repo)

@router.get("/", response_model=List[VehiculoResponse])
def listar(service: VehiculoService = Depends(get_vehiculo_service)):
    return service.listar_todo()

@router.post("/", response_model=VehiculoResponse)
def crear(datos: VehiculoCreate, service: VehiculoService = Depends(get_vehiculo_service)):
    return service.crear_nuevo(datos)

@router.delete("/{vehiculo_id}", status_code=204)
def eliminar(vehiculo_id: int, service: VehiculoService = Depends(get_vehiculo_service)):
    # Aquí podrías agregar lógica en el service para validar antes de borrar
    db_vehiculo = service.repo.get_by_id(vehiculo_id)
    if not db_vehiculo:
        raise HTTPException(status_code=404, detail="Vehículo no encontrado")
    service.repo.delete(db_vehiculo)
    return None