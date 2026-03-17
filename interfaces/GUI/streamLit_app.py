import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.title("Sistema de Concesionario 🚗")

menu = st.sidebar.selectbox(
    "Menú",
    ["Ver Vehículos", "Agregar Vehículo", "Actualizar Precio", "Vender Vehículo"]
)

# 🔍 VER VEHÍCULOS
if menu == "Ver Vehículos":
    if st.button("Cargar vehículos"):
        res = requests.get(f"{API_URL}/vehiculos")

        if res.status_code == 200:
            vehiculos = res.json()
            st.write(vehiculos)
        else:
            st.error("Error al obtener datos")


# ➕ AGREGAR VEHÍCULO
elif menu == "Agregar Vehículo":
    id_vehiculo = st.number_input("ID", step=1)
    marca = st.text_input("Marca")
    modelo = st.text_input("Modelo")
    anio = st.number_input("Año", step=1)
    kilometraje = st.number_input("Kilometraje", step=1)
    precio = st.number_input("Precio")

    if st.button("Guardar"):
        res = requests.post(f"{API_URL}/vehiculos", json={
            "id_vehiculo": id_vehiculo,
            "marca": marca,
            "modelo": modelo,
            "anio": anio,
            "kilometraje": kilometraje,
            "precio": precio
        })

        if res.status_code == 200:
            st.success("Vehículo agregado")
        else:
            st.error(res.json()["detail"])


# 💰 ACTUALIZAR PRECIO
elif menu == "Actualizar Precio":
    id_vehiculo = st.number_input("ID del vehículo", step=1)
    nuevo_precio = st.number_input("Nuevo precio")

    if st.button("Actualizar"):
        res = requests.put(
            f"{API_URL}/vehiculos/{id_vehiculo}/precio",
            params={"nuevo_precio": nuevo_precio}
        )

        if res.status_code == 200:
            st.success("Precio actualizado")
        else:
            st.error(res.json()["detail"])


# 🛒 VENDER VEHÍCULO
elif menu == "Vender Vehículo":
    id_vehiculo = st.number_input("ID del vehículo", step=1)

    if st.button("Vender"):
        res = requests.put(f"{API_URL}/vehiculos/{id_vehiculo}/vender")

        if res.status_code == 200:
            st.success("Vehículo vendido")
        else:
            st.error(res.json()["detail"])