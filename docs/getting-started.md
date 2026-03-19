#  ¿Como ejecutar?

Sigue estos pasos para ejecutar el concesionario en tu máquina local. Usamos `uv` para una gestión de dependencias ultra rápida.

## Instalación

=== "Windows"

    ```powershell
    # Clona el repositorio
    git clone [https://github.com/TU_USUARIO/Sistema-de-Gestion-para-un-Concesionario-de-Carros-Usados.git](https://github.com/TU_USUARIO/Sistema-de-Gestion-para-un-Concesionario-de-Carros-Usados.git)
    cd Sistema-de-Gestion-para-un-Concesionario-de-Carros-Usados

    # Sincroniza las dependencias
    uv sync

    # Ejecuta la ayuda de la CLI
    uv run python main.py --help
    ```

=== "MacOS / Linux"

    ```bash
    # Clona el repositorio
    git clone [https://github.com/TU_USUARIO/Sistema-de-Gestion-para-un-Concesionario-de-Carros-Usados.git](https://github.com/TU_USUARIO/Sistema-de-Gestion-para-un-Concesionario-de-Carros-Usados.git)
    cd Sistema-de-Gestion-para-un-Concesionario-de-Carros-Usados

    # Sincroniza las dependencias
    uv sync

    # Ejecuta la ayuda de la CLI
    uv run python main.py --help
    ```

!!! tip "Primer Comando"
    Te recomendamos empezar listando los vehículos disponibles usando `uv run python main.py listar`.