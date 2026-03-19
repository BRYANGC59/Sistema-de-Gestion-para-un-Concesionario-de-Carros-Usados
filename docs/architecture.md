#  Arquitectura del Sistema

El proyecto sigue estrictamente el patrón **Clean `src` Layout** para separar las responsabilidades.

## Diagrama de Flujo

El siguiente diagrama ilustra cómo viaja la información desde que el usuario digita un comando hasta que se guarda en el archivo local:

```mermaid
flowchart LR
    A[CLI / main.py] --> B(Services)
    B --> C{Models}
    B --> D[(Storage JSON)]
    C -.-> |Valida datos| B