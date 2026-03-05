from typing import List
from src.mi_app.models import VehiculoUsado, EstadoVehiculo
from src.mi_app.storage import cargar_datos, guardar_datos
from src.mi_app.exceptions import (
    VehiculoNoEncontradoError,
    VehiculoYaVendidoError,
    PrecioInvalidoError,
    IdDuplicadoError
)


class InventarioService:
    def __init__(self):
        self._datos_crudos = cargar_datos()
        self.vehiculos: List[VehiculoUsado] = []

        for v in self._datos_crudos:
            estado_texto = v.get("estado", EstadoVehiculo.DISPONIBLE.value)
            v["estado"] = EstadoVehiculo(estado_texto)
            self.vehiculos.append(VehiculoUsado(**v))

    def _guardar(self) -> None:
        datos_a_guardar = []
        for v in self.vehiculos:
            diccionario = {
                "id_vehiculo": v.id_vehiculo,
                "marca": v.marca,
                "modelo": v.modelo,
                "anio": v.anio,
                "kilometraje": v.kilometraje,
                "precio": v.precio,
                "estado": v.estado.value
            }
            datos_a_guardar.append(diccionario)
        guardar_datos(datos_a_guardar)

    def listar_disponibles(self) -> List[VehiculoUsado]:
        return [v for v in self.vehiculos if v.estado == EstadoVehiculo.DISPONIBLE]

    def buscar_por_id(self, id_vehiculo: int) -> VehiculoUsado:
        for v in self.vehiculos:
            if v.id_vehiculo == id_vehiculo:
                return v
        raise VehiculoNoEncontradoError(f"El vehículo con ID {id_vehiculo} no existe en el lote.")

    def agregar_vehiculo(
            self, id_vehiculo: int, marca: str, modelo: str,
            anio: int, kilometraje: int, precio: float
    ) -> VehiculoUsado:
        for v in self.vehiculos:
            if v.id_vehiculo == id_vehiculo:
                raise IdDuplicadoError(f"Ya existe un vehículo registrado con el ID {id_vehiculo}.")

        if precio < 0:
            raise PrecioInvalidoError("El precio de un vehículo no puede ser negativo.")

        nuevo_vehiculo = VehiculoUsado(
            id_vehiculo=id_vehiculo,
            marca=marca,
            modelo=modelo,
            anio=anio,
            kilometraje=kilometraje,
            precio=precio,
            estado=EstadoVehiculo.DISPONIBLE
        )

        self.vehiculos.append(nuevo_vehiculo)
        self._guardar()
        return nuevo_vehiculo

    def actualizar_precio(self, id_vehiculo: int, nuevo_precio: float) -> VehiculoUsado:
        if nuevo_precio < 0:
            raise PrecioInvalidoError("El nuevo precio no puede ser negativo.")

        vehiculo = self.buscar_por_id(id_vehiculo)
        vehiculo.precio = nuevo_precio

        self._guardar()
        return vehiculo

    def vender_vehiculo(self, id_vehiculo: int) -> VehiculoUsado:
        vehiculo = self.buscar_por_id(id_vehiculo)

        if vehiculo.estado == EstadoVehiculo.VENDIDO:
            raise VehiculoYaVendidoError(f"El vehículo '{vehiculo.marca} {vehiculo.modelo}' ya fue vendido.")

        vehiculo.estado = EstadoVehiculo.VENDIDO
        self._guardar()
        return vehiculo