from sqlmodel import Session, select
from api.storage.models.venta import Venta
from typing import List


class VentaRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_all(self) -> List[Venta]:
        return self.session.exec(select(Venta)).all()

    def create(self, venta: Venta) -> Venta:
        self.session.add(venta)
        self.session.commit()
        self.session.refresh(venta)
        return venta