import streamlit as st
import requests
from datetime import datetime

import streamlit as st
import requests

# --- SECCIÓN: PARTIDOS EN VIVO ---
st.title("📺 Partidos del Día")
st.write("Acá podés ver los partidos programados para hoy y sus resultados en tiempo real.")

# 1. Acordate de poner tu token real acá adentro (dejando las comillas):
API_TOKEN = "TU_TOKEN_REAL_ACA" 

def cargar_partidos_hoy():
    url = "https://api.football-data.org/v4/matches"
    headers = {"X-Auth-Token": API_TOKEN}
    
    try:
        response = requests.get(url, headers=headers)
        
        # Si la API responde con un error, nos avisa acá
        if response.status_code != 200:
            st.error(f"🚨 Error de la API (Código {response.status_code}): {response.text}")
            return []
            
        return response.json().get("matches", [])
    except Exception as e:
        st.error(f"❌ Error de conexión general: {e}")
        return []

# 🔑 ¡ESTA ES LA LÍNEA QUE SE HABÍA BORRADO! 
# Creamos la variable ejecutando la función:
lista_partidos = cargar_partidos_hoy()

# 2. Ahora que la variable EXISTE, mostramos los resultados o el plan B
if lista_partidos:
    for partido in lista_partidos:
        competicion = partido["competition"]["name"]
        equipo_local = partido["homeTeam"]["name"]
        equipo_vis = partido["awayTeam"]["name"]
        estado = partido["status"]
        
        if estado == "FINISHED":
            goles_local = partido["score"]["fullTime"]["home"]
            goles_vis = partido["score"]["fullTime"]["away"]
            info_partido = f"🏁 **Finalizado:** {goles_local} - {goles_vis}"
            
        elif estado == "IN_PLAY" or estado == "PAUSED":
            goles_local = partido["score"]["fullTime"]["home"]
            goles_vis = partido["score"]["fullTime"]["away"]
            info_partido = f"🔴 **En Vivo:** {goles_local} - {goles_vis}"
            
        else:
            hora_utc = partido["utcDate"].split("T")[1][:5]
            info_partido = f"⏰ **Próximamente:** {hora_utc} UTC"
        
        with st.container():
            st.markdown(f"🏆 *{competicion}*")
            st.subheader(f"{equipo_local}  vs  {equipo_vis}")
            st.write(info_partido)
            st.divider()
else:
    # Si la lista viene vacía porque no hay partidos de esas ligas hoy
    st.write("Podés revisar el minuto a minuto de forma externa acá:")
    
    col1, col2 = st.columns(2)
    with col1:
        st.link_button("🇦🇷 Ver en Promiedos", "https://www.promiedos.com.ar")
    with col2:
        st.link_button("🌐 Ver en Flashscore", "https://www.flashscore.com")

# 1. Configura tu token gratuito acá abajo:
# (Pegá acá adentro el código que te llegó por mail)
API_TOKEN = "a1b2c3d4e5f6g7h8i9j0"

def cargar_partidos_hoy():
    url = "https://api.football-data.org/v4/matches"
    headers = {"X-Auth-Token": API_TOKEN}
    
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json().get("matches", [])
        else:
            return []
    except:
        return []

# Llamamos a la API para traer la lista
def cargar_partidos_hoy():
    url = "https://api.football-data.org/v4/matches"
    headers = {"X-Auth-Token": API_TOKEN}
    
    try:
        response = requests.get(url, headers=headers)
        
        # SI LA API RESPONDE CON ERROR (Ej: Código 400, 403, 429)
        if response.status_code != 200:
            st.error(f"🚨 Error de la API (Código {response.status_code}): {response.text}")
            return []
            
        partidos = response.json().get("matches", [])
        
        # SI LA API CONECTÓ BIEN PERO NO HAY PARTIDOS HOY
        if not partidos:
            st.warning("⚠️ La API funciona perfecto, pero hoy no hay partidos programados en sus ligas gratuitas.")
            
        return partidos
    except Exception as e:
        st.error(f"❌ Error de conexión general: {e}")
        return []


if lista_partidos:
    # Si la API devolvió partidos, los mostramos organizados
    for partido in lista_partidos:
        competicion = partido["competition"]["name"]
        equipo_local = partido["homeTeam"]["name"]
        equipo_vis = partido["awayTeam"]["name"]
        estado = partido["status"]
        
        # Traducimos y formateamos los resultados según el estado del partido
        if estado == "FINISHED":
            goles_local = partido["score"]["fullTime"]["home"]
            goles_vis = partido["score"]["fullTime"]["away"]
            info_partido = f"🏁 **Finalizado:** {goles_local} - {goles_vis}"
            
        elif estado == "IN_PLAY" or estado == "PAUSED":
            goles_local = partido["score"]["fullTime"]["home"]
            goles_vis = partido["score"]["fullTime"]["away"]
            info_partido = f"🔴 **En Vivo:** {goles_local} - {goles_vis}"
            
        else:
            # Si todavía no empezó, extraemos la hora (viene en formato UTC)
            hora_utc = partido["utcDate"].split("T")[1][:5]
            info_partido = f"⏰ **Próximamente:** {hora_utc} UTC"
        
        # Mostramos el partido de forma estética
        with st.container():
            st.markdown(f"🏆 *{competicion}*")
            st.subheader(f"{equipo_local}  vs  {equipo_vis}")
            st.write(info_partido)
            st.divider()
else:
    # Si la API falla o no hay partidos hoy, mostramos un aviso y los botones de respaldo
    st.info("No se pudieron sincronizar partidos automáticos para hoy o la API alcanzó su límite gratuito.")
    st.write("Podés revisar el minuto a minuto de forma externa acá:")
    
    col1, col2 = st.columns(2)
    with col1:
        st.link_button("🇦🇷 Ver en Promiedos", "https://www.promiedos.com.ar")
    with col2:
        st.link_button("🌐 Ver en Flashscore", "https://www.flashscore.com")
        
