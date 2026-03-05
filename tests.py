import pytest
from src.mi_app.services import InventarioService
from src.mi_app.models import EstadoVehiculo
from src.mi_app.exceptions import (
    VehiculoNoEncontradoError,
    VehiculoYaVendidoError,
    PrecioInvalidoError,
    IdDuplicadoError
)


@pytest.fixture
def servicio_test(tmp_path, monkeypatch):
    ruta_falsa = tmp_path / "test_database.json"
    monkeypatch.setattr("src.mi_app.storage.DB_PATH", ruta_falsa)
    return InventarioService()


def test_01_agregar_vehiculo_exitoso(servicio_test):
    servicio_test.agregar_vehiculo(1, "Chevrolet", "Sail", 2022, 30000, 35000000.0)

    disponibles = servicio_test.listar_disponibles()
    assert len(disponibles) == 1
    assert disponibles[0].modelo == "Sail"
    assert disponibles[0].estado == EstadoVehiculo.DISPONIBLE


def test_02_buscar_vehiculo_por_id_exitoso(servicio_test):
    servicio_test.agregar_vehiculo(1, "Chevrolet", "Onix", 2023, 15000, 45000000.0)

    vehiculo = servicio_test.buscar_por_id(1)
    assert vehiculo.marca == "Chevrolet"
    assert vehiculo.modelo == "Onix"


def test_03_actualizar_precio_exitoso(servicio_test):
    servicio_test.agregar_vehiculo(1, "Renault", "Sandero", 2021, 40000, 38000000.0)

    servicio_test.actualizar_precio(1, 36500000.0)
    vehiculo = servicio_test.buscar_por_id(1)

    assert vehiculo.precio == 36500000.0


def test_04_vender_vehiculo_exitoso(servicio_test):
    servicio_test.agregar_vehiculo(1, "Mazda", "3", 2020, 50000, 60000000.0)

    servicio_test.vender_vehiculo(1)

    vehiculo = servicio_test.buscar_por_id(1)
    disponibles = servicio_test.listar_disponibles()

    assert vehiculo.estado == EstadoVehiculo.VENDIDO
    assert len(disponibles) == 0


def test_05_listar_inventario_vacio(servicio_test):
    disponibles = servicio_test.listar_disponibles()
    assert isinstance(disponibles, list)
    assert len(disponibles) == 0


def test_06_kilometraje_cero_permitido(servicio_test):
    servicio_test.agregar_vehiculo(1, "Toyota", "Corolla", 2024, 0, 90000000.0)

    vehiculo = servicio_test.buscar_por_id(1)
    assert vehiculo.kilometraje == 0


def test_07_actualizar_precio_vehiculo_inexistente(servicio_test):
    """7. Extraordinario: Intentar cambiar el precio a un ID que no existe lanza error."""
    with pytest.raises(VehiculoNoEncontradoError):
        servicio_test.actualizar_precio(999, 40000000.0)


def test_08_buscar_vehiculo_inexistente_lanza_error(servicio_test):
    servicio_test.agregar_vehiculo(1, "Chevrolet", "Sail", 2022, 30000, 35000000.0)

    with pytest.raises(VehiculoNoEncontradoError):
        servicio_test.buscar_por_id(99)


def test_09_error_agregar_id_duplicado(servicio_test):
    servicio_test.agregar_vehiculo(1, "Chevrolet", "Onix", 2023, 15000, 45000000.0)

    with pytest.raises(IdDuplicadoError):
        servicio_test.agregar_vehiculo(1, "Chevrolet", "Spark", 2019, 60000, 25000000.0)


def test_10_error_precio_negativo(servicio_test):
    with pytest.raises(PrecioInvalidoError):
        servicio_test.agregar_vehiculo(1, "Kia", "Picanto", 2021, 20000, -5000.0)


def test_11_vender_vehiculo_ya_vendido(servicio_test):
    servicio_test.agregar_vehiculo(1, "Ford", "Fiesta", 2018, 70000, 32000000.0)
    servicio_test.vender_vehiculo(1)

    with pytest.raises(VehiculoYaVendidoError):
        servicio_test.vender_vehiculo(1)