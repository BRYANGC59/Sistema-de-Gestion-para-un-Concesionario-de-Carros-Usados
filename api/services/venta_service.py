from fastapi import HTTPException
from api.storage.repositories.venta_repo import VentaRepository
from api.storage.repositories.vehiculo_repo import VehiculoRepository
from api.storage.models.venta import Venta


class VentaService:
    def __init__(self, venta_repo: VentaRepository, vehiculo_repo: VehiculoRepository):
        self.venta_repo = venta_repo
        self.vehiculo_repo = vehiculo_repo

    def procesar_venta(self, datos_venta):
        # 1. Buscar el carro
        carro = self.vehiculo_repo.get_by_id(datos_venta.carro_id)
        if not carro or carro.estado != "Disponible":
            raise HTTPException(status_code=400, detail="Carro no disponible para venta")

        # 2. Cambiar estado a Vendido
        self.vehiculo_repo.update(carro, {"estado": "Vendido"})

        # 3. Guardar la venta
        nueva_venta = Venta(**datos_venta.model_dump())
        return self.venta_repo.create(nueva_venta)