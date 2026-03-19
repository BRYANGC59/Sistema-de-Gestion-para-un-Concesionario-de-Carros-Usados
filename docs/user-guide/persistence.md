
# Capa de Persistencia

Para mantener la simplicidad y cumplir con los requisitos del proyecto, el sistema utiliza un archivo de texto plano para almacenar la información, simulando una base de datos local.

## Archivo `database.json`
Toda la información del inventario reside en el archivo `data/database.json`. El módulo `storage.py` es el único autorizado por la arquitectura para leer (`cargar_datos`) y escribir (`guardar_datos`) en este archivo.

### Estructura de los Datos
Los modelos en memoria (Dataclasses) se serializan a diccionarios de Python antes de ser guardados. El formato final es una lista de objetos JSON.

**Ejemplo de estructura:**
```json
[
  {
    "id_vehiculo": 2,
    "marca": "Chevrolet",
    "modelo": "Sail",
    "anio": 2020,
    "kilometraje": 45000,
    "precio": 35000000,
    "estado": "Disponible"
  },
  {
    "id_vehiculo": 3,
    "marca": "Chevrolet",
    "modelo": "Spark",
    "anio": 2018,
    "kilometraje": 70000,
    "precio": 25000000,
    "estado": "Vendido"
  }
]