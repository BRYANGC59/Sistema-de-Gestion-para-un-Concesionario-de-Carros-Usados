from sqlmodel import Session, select
from api.storage.models.cliente import Cliente
from typing import List, Optional

class ClienteRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_all(self) -> List[Cliente]:
        return self.session.exec(select(Cliente)).all()

    def get_by_id(self, cedula: int) -> Optional[Cliente]:
        return self.session.get(Cliente, cedula)

    def create(self, cliente: Cliente) -> Cliente:
        self.session.add(cliente)
        self.session.commit()
        self.session.refresh(cliente)
        return cliente

    def update(self, db_cliente: Cliente, data: dict) -> Cliente:
        for key, value in data.items():
            setattr(db_cliente, key, value)
        self.session.add(db_cliente)
        self.session.commit()
        self.session.refresh(db_cliente)
        return db_cliente

    def delete(self, cliente: Cliente):
        self.session.delete(cliente)
        self.session.commit()