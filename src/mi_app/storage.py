import json
from typing import List, Dict, Any
from pathlib import Path

DB_PATH = Path("data/database.json")

def cargar_datos() -> List[Dict[str, Any]]:
    if not DB_PATH.exists():
        return []
    with open(DB_PATH, "r", encoding="utf-8") as file:
        return json.load(file)

def guardar_datos(datos: List[Dict[str, Any]]) -> None:
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(DB_PATH, "w", encoding="utf-8") as file:
        json.dump(datos, file, indent=4)