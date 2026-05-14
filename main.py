from fastapi import FastAPI
from api.routers import vehiculos # Luego importamos clientes y ventas

app = FastAPI(title="API Concesionario Medellín")

# Conectar las rutas
app.include_router(vehiculos.router)

@app.get("/")
def home():
    return {"mensaje": "API funcionando. Ve a /docs para la documentación."}