import os
from dotenv import load_dotenv
from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import Session, select, SQLModel, create_engine
from typing import List
from src.mi_app.models.vehiculo import Vehiculo, EstadoVehiculo
from src.mi_app.models.cliente import Cliente
from src.mi_app.models.venta import Venta

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

if DATABASE_URL is None:
    raise ValueError("¡Falta la variable DATABASE_URL en el archivo .env!")

engine = create_engine(DATABASE_URL)

app = FastAPI(
    title="API Concesionario",
    description="Sistema de gestión de vehículos usados",
    version="1.0.0"
)

# 3. Crear las tablas al iniciar el servidor (si no existen)
@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)

# 4. Dependencia para obtener la sesión de la base de datos
def get_session():
    with Session(engine) as session:
        yield session

# --- RUTAS (ENDPOINTS) ---

@app.post("/vehiculos/", response_model=Vehiculo, tags=["Inventario"])
def agregar_vehiculo(vehiculo: Vehiculo, session: Session = Depends(get_session)):
    """
    Registra un nuevo carro en Supabase.
    Si el precio o kilometraje son negativos, FastAPI lanzará un error automáticamente.
    """
    session.add(vehiculo)
    session.commit()
    session.refresh(vehiculo) # Refresca para obtener el ID generado por la base de datos
    return vehiculo

@app.get("/", tags=["Inicio"])
def mensaje_bienvenida():
    return {"mensaje": "¡Bienvenido a la API del Concesionario! Ve a /docs para ver la documentación."}

@app.get("/vehiculos/disponibles", response_model=List[Vehiculo], tags=["Inventario"])
def listar_disponibles(session: Session = Depends(get_session)):
    """
    Devuelve todos los vehículos que tienen estado 'Disponible'.
    """
    statement = select(Vehiculo).where(Vehiculo.estado == EstadoVehiculo.DISPONIBLE)
    resultados = session.exec(statement).all()
    return resultados