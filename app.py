import streamlit as st
import requests

# --- SECCIÓN: PARTIDOS EN VIVO ---
st.title("📺 Partidos del Día")
st.write("Acá podés ver los partidos programados para hoy y sus resultados en tiempo real.")

# ⚠️ PASO CLAVE: Reemplazá este texto largo de ejemplo por las letras y números reales
# que te llegaron al mail desde football-data.org. Asegurate de no borrar las comillas.
API_TOKEN = "AQUÍ_VA_TU_CÓDIGO_ALFANUMÉRICO_REAL" 

def cargar_partidos_hoy():
    url = "https://api.football-data.org/v4/matches"
    headers = {"X-Auth-Token": API_TOKEN}
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json().get("matches", [])
        return []
    except:
        return []

lista_partidos = cargar_partidos_hoy()

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
    # Este plan B solo aparece si la lista viene vacía o el token falla
    st.info("No hay partidos de ligas principales para mostrar en este momento.")
    st.write("Podés revisar el minuto a minuto de forma externa acá:")
    col1, col2 = st.columns(2)
    with col1:
        st.link_button("🇦🇷 Ver en Promiedos", "https://www.promiedos.com.ar")
    with col2:
        st.link_button("🌐 Ver en Flashscore", "https://www.flashscore.com")
