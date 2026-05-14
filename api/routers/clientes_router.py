from fastapi import APIRouter, Depends
from sqlmodel import Session
from typing import List

from api.storage.database import get_session
from api.storage.repositories.cliente_repo import ClienteRepository
from api.services.cliente_service import ClienteService
from api.schemas.cliente_schema import ClienteCreate, ClienteResponse

router = APIRouter(prefix="/clientes", tags=["Clientes"])

def get_cliente_service(session: Session = Depends(get_session)):
    repo = ClienteRepository(session)
    return ClienteService(repo)

@router.get("/", response_model=List[ClienteResponse])
def listar_clientes(service: ClienteService = Depends(get_cliente_service)):
    return service.listar_todos_los_clientes()

@router.post("/", response_model=ClienteResponse)
def registrar_cliente(datos: ClienteCreate, service: ClienteService = Depends(get_cliente_service)):
    return service.registrar_nuevo_cliente(datos)

@router.get("/{cedula}", response_model=ClienteResponse)
def obtener_cliente(cedula: int, service: ClienteService = Depends(get_cliente_service)):
    return service.buscar_por_cedula(cedula)