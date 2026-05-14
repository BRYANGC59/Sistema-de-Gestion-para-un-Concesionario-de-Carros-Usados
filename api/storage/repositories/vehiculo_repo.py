from sqlmodel import Session, select
from api.storage.models.vehiculo import Vehiculo  # 👈 Importas tu modelo separado
from typing import List


class VehiculoRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_all(self) -> List[Vehiculo]:
        return self.session.exec(select(Vehiculo)).all()

    def create(self, vehiculo: Vehiculo) -> Vehiculo:
        self.session.add(vehiculo)
        self.session.commit()
        self.session.refresh(vehiculo)
        return vehiculo
