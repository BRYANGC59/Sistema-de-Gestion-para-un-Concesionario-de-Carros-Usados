from fastapi import APIRouter, Depends
from sqlmodel import Session
from typing import List

from api.storage.database import get_session
from api.storage.repositories.venta_repo import VentaRepository
from api.storage.repositories.vehiculo_repo import VehiculoRepository
from api.services.venta_service import VentaService
from api.schemas.venta_schema import VentaCreate, VentaResponse

router = APIRouter(prefix="/ventas", tags=["Ventas"])

def get_venta_service(session: Session = Depends(get_session)):
    v_repo = VentaRepository(session)
    veh_repo = VehiculoRepository(session)
    return VentaService(v_repo, veh_repo)

@router.post("/", response_model=VentaResponse)
def realizar_venta(datos: VentaCreate, service: VentaService = Depends(get_venta_service)):
    return service.procesar_venta(datos)

@router.get("/", response_model=List[VentaResponse])
def historial_ventas(service: VentaService = Depends(get_venta_service)):
    return service.venta_repo.get_all()