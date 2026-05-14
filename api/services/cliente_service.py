from fastapi import HTTPException
from api.storage.repositories.cliente_repo import ClienteRepository
from api.storage.models.cliente import Cliente
from api.schemas.cliente_schema import ClienteCreate


class ClienteService:
    def __init__(self, repository: ClienteRepository):
        self.repo = repository

    def listar_todos_los_clientes(self):
        """Obtiene la lista completa de clientes."""
        return self.repo.get_all()

    def buscar_por_cedula(self, cedula: int):
        """Busca un cliente específico y lanza error si no existe."""
        cliente = self.repo.get_by_id(cedula)
        if not cliente:
            raise HTTPException(
                status_code=404,
                detail=f"No se encontró ningún cliente con la cédula {cedula}"
            )
        return cliente

    def registrar_nuevo_cliente(self, datos: ClienteCreate):
        """Verifica que la cédula no esté duplicada antes de crear."""
        existente = self.repo.get_by_id(datos.cedula)
        if existente:
            raise HTTPException(
                status_code=400,
                detail="Ya existe un cliente registrado con esta cédula"
            )

        # Convertimos el esquema de Pydantic a modelo de SQLModel
        nuevo_cliente = Cliente(**datos.model_dump())
        return self.repo.create(nuevo_cliente)

    def actualizar_cliente(self, cedula: int, datos_nuevos: dict):
        """Actualiza la información de un cliente existente."""
        db_cliente = self.buscar_por_cedula(cedula)
        return self.repo.update(db_cliente, datos_nuevos)

    def eliminar_cliente(self, cedula: int):
        """Elimina permanentemente a un cliente del sistema."""
        db_cliente = self.buscar_por_cedula(cedula)
        self.repo.delete(db_cliente)