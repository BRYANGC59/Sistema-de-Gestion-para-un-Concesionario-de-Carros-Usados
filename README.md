# Sistema_de_Gestion_para_Concesionario_de_Carros_Usados

-Sistema de Gestión de Inventario para Concesionario (CLI)

## Propósito y Alcance del Proyecto
Este proyecto es una aplicación de terminal (CLI) diseñada para facilitar el control de inventario en un concesionario de carros usados. Su objetivo principal es reemplazar las complicadas hojas de cálculo por una herramienta rápida y visual directamente en la consola.

Con esta aplicación, un usuario puede realizar las cuatro operaciones básicas (CRUD) de manera sencilla:
- **Registrar** nuevos vehículos que ingresan al lote.
- **Consultar** el inventario disponible en tiempo real con tablas fáciles de leer.
- **Actualizar** los precios de los carros según el mercado.
- **Vender** (eliminar del inventario activo) los vehículos una vez se concreta un negocio.

Todo esto está construido asegurando que los datos se guarden de forma segura en un archivo local, manteniendo el historial del concesionario organizado.

**Manual de Uso de la CLI**

1. Agregar un vehículo nuevo:

uv run python main.py agregar --id 1 --marca "Chevrolet" --modelo "Onix" --anio 2023 --kilometraje 15000 --precio 45000000

3. Listar los vehiculos disponibles:

uv run python main.py listar

4. Buscar un carro especifico:

uv run python main.py buscar --id 2

5. Actualizar precio:

uv run python main.py actualizar-precio --id 1 --nuevo-precio 43500000

6. Registrar una venta:

uv run python main.py vender --id 1

**INSTRUCCION PARA PRUEBAS UNITARIAS**

uv run pytest
