import streamlit as st
import requests

# --- SECCIÓN: PARTIDOS Y TORNEOS ---
st.title("⚽ Partidos y Torneos en Vivo")
st.write("Seguí los partidos del Mundial, ligas y torneos más importantes del mundo hoy.")

# ⚠️ Colocá acá tu token real de football-data.org (dejando las comillas)
API_TOKEN = "TU_TOKEN_REAL_ACA" 

def cargar_todos_los_partidos():
    url = "https://api.football-data.org/v4/matches"
    headers = {"X-Auth-Token": API_TOKEN}
    try:
        response = requests.get(url, headers=headers)
        
        # Si el token falla, nos avisa con el cartel rojo
        if response.status_code != 200:
            st.error(f"🚨 Error de la API (Código {response.status_code}): {response.text}")
            return {}
            
        partidos = response.json().get("matches", [])
        
        # Agrupamos los partidos por el nombre de su competición
        partidos_agrupados = {}
        for partido in partidos:
            nombre_torneo = partido["competition"]["name"]
            if nombre_torneo not in partidos_agrupados:
                partidos_agrupados[nombre_torneo] = []
            partidos_agrupados[nombre_torneo].append(partido)
            
        return partidos_agrupados
    except:
        return {}

# Llamamos a la API para traer el diccionario organizado
torneos_hoy = cargar_todos_los_partidos()

if torneos_hoy:
    # Recorremos cada torneo y creamos una sección para cada uno
    for torneo, partidos in torneos_hoy.items():
        # Usamos expanders para que la app quede súper limpia y scrolleable
        with st.expander(f"🏆 {torneo} ({len(partidos)} partidos)", expanded=True):
            for partido in partidos:
                equipo_local = partido["homeTeam"]["name"]
                equipo_vis = partido["awayTeam"]["name"]
                estado = partido
                
