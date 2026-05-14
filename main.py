from fastapi import FastAPI
from api.routers import vehiculos_router, clientes_router, ventas_router
from api.storage.database import engine
from sqlmodel import SQLModel

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

app = FastAPI(
    title="🚗 API AG Vehiculos Usados",
    description="Sistema modular para la gestión de vehículos, clientes y ventas.",
    version="1.0.0"
)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()


app.include_router(vehiculos_router.router)
app.include_router(clientes_router.router)
app.include_router(ventas_router.router)

@app.get("/", tags=["Inicio"])
def read_root():
    return {"mensaje": "¡Bienvenido al sistema del Concesionario! Visita /docs para interactuar."}