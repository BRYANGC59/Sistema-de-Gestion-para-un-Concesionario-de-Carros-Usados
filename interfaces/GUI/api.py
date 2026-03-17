from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from src.mi_app.services import InventarioService
from src.mi_app.exceptions import (
    VehiculoNoEncontradoError,
    VehiculoYaVendidoError,
    PrecioInvalidoError,
    IdDuplicadoError
)

app = FastAPI()
service = InventarioService()

class VehiculoCreate(BaseModel):
    id_vehiculo: int
    marca: str
    modelo: str
    anio: int
    kilometraje: int
    precio: float

@app.get("/vehiculos")
def listar():
    return [v.__dict__ for v in service.listar_disponibles()]

@app.post("/vehiculos")
def agregar(v: VehiculoCreate):
    try:
        nuevo = service.agregar_vehiculo(
            v.id_vehiculo, v.marca, v.modelo,
            v.anio, v.kilometraje, v.precio
        )
        return nuevo.__dict__

    except IdDuplicadoError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except PrecioInvalidoError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.put("/vehiculos/{id_vehiculo}/precio")
def actualizar_precio(id_vehiculo: int, nuevo_precio: float):
    try:
        v = service.actualizar_precio(id_vehiculo, nuevo_precio)
        return v.__dict__

    except VehiculoNoEncontradoError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except PrecioInvalidoError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.put("/vehiculos/{id_vehiculo}/vender")
def vender(id_vehiculo: int):
    try:
        v = service.vender_vehiculo(id_vehiculo)
        return v.__dict__

    except VehiculoNoEncontradoError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except VehiculoYaVendidoError as e:
        raise HTTPException(status_code=400, detail=str(e))