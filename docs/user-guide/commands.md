#  Comandos de la CLI

El sistema funciona a través de una interfaz de línea de comandos (CLI). A continuación, se detallan las operaciones principales para gestionar el inventario del concesionario.

## Agregar un Vehículo
Permite registrar un nuevo carro en el sistema. El vehículo ingresará automáticamente con estado `Disponible`.

**Comando:**
```bash
uv run python main.py agregar --id 1 --marca "Hyundai" --modelo "HB20" --anio 2023 --kilometraje 12800 --precio 67900000
``` 

## Listar Vehículos Disponibles
Muestra todos los carros que están listos para la venta, ocultando aquellos que ya fueron vendidos.

**Comando:**
```bash
uv run python main.py listar
```

## Vender un Vehiculo
Cambia el estado del carro a Vendido 

**Comando:**
```bash
uv run python main.py vender --id 1
```

