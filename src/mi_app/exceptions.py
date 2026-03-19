class VehiculoNoEncontradoError(Exception):
    """Se lanza cuando se busca un ID que no existe en el inventario."""
    pass

class PrecioInvalidoError(Exception):
    """Se lanza cuando se intenta asignar un precio negativo a un vehículo."""
    pass

class IdDuplicadoError(Exception):
    """Se lanza cuando se intenta registrar un vehículo con un ID ya existente."""
    pass

class VehiculoYaVendidoError(Exception):
    """Se lanza cuando se intenta vender un vehículo que ya tiene estado VENDIDO."""
    pass