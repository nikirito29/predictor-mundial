import streamlit as st
import requests

# Configuración inicial de estilo (Opcional, sumará al look de app móvil)
st.markdown("""
    <style>
    .block-container { padding-top: 2rem; padding-bottom: 2rem; }
    </style>
""", unsafe_allow_html=True)

# --- 1. BANNER DESTACADO (Arriba de todo) ---
st.markdown("### 🔥 Partido Destacado de Hoy")
with st.container(border=True):
    col_A, col_B = st.columns([2, 1])
    with col_A:
        st.markdown("🇦🇷 **Argentina vs. Cabo Verde**")
        st.caption("🏆 Fase de Grupos • ¡Pronósticos abiertos!")
    with col_B:
        st.button("🎯 Predecir", key="btn_destacado", use_container_width=True)

st.write("") # Espacio visual

# --- 2. SECCIONES POR PESTAÑAS (Estilo selector de deportes) ---
st.markdown("### 📊 Competiciones")
tab_mundial, tab_ligas, tab_externo = st.tabs([
    "🏆 Mundial 2026", 
    "🇪🇺 Ligas Europeas", 
    "🌐 Enlaces Externos"
])

# ⚠️ Tu Token Real de la API
API_TOKEN = "TU_TOKEN_REAL_ACA" 

def obtener_partidos():
    url = "https://api.football-data.org/v4/matches"
    headers = {"X-Auth-Token": API_TOKEN}
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json().get("matches", [])
        return []
    except:
        return []

# Traemos la información una sola vez
todos_los_partidos = obtener_partidos()


# --- PESTAÑA 1: MUNDIAL ---
with tab_mundial:
    partidos_wc = [p for p in todos_los_partidos if p.get("competition", {}).get("code") == "WC"]
    
    if partidos_wc:
        for partido in partidos_wc:
            local = partido["homeTeam"]["name"]
            visita = partido["awayTeam"]["name"]
            estado = partido["status"]
            
            # Formateo de marcador según estado
            if estado in ["IN_PLAY", "PAUSED", "FINISHED"]:
                g_local = partido["score"]["fullTime"]["home"]
                g_visita = partido["score"]["fullTime"]["away"]
                marcador = f"**{g_local} - {g_visita}**"
                badge = "🔴 EN VIVO" if estado != "FINISHED" else "🏁 FIN"
            else:
                marcador = "vs"
                badge = f"⏰ {partido['utcDate'].split('T')[1][:5]} UTC"

            # Creamos la "cajita" o tarjeta individual para el partido
            with st.container(border=True):
                c1, c2, c3 = st.columns([3, 2, 3])
                with c1:
                    st.markdown(f"<p style='text-align: right;'><b>{local}</b></p>", unsafe-allow_html=True)
                with c2:
                    st.markdown(f"<p style='text-align: center;'>{marcador}<br><small>{badge}</small></p>", unsafe-allow_html=True)
                with c3:
                    st.markdown(f"<p style='text-align: left;'><b>{visita}</b></p>", unsafe-allow_html=True)
    else:
        st.info("No hay partidos del Mundial programados para hoy en la API.")


# --- PESTAÑA 2: LIGAS EUROPEAS ---
with tab_ligas:
    # Filtramos para excluir el mundial y mostrar torneos como Premier (PL), Champions (CL), etc.
    partidos_ligas = [p for p in todos_los_partidos if p.get("competition", {}).get("code") != "WC"]
    
    if partidos_ligas:
        # Agrupamos por liga para poner un subtítulo por torneo
        ligas_agrupadas = {}
        for p in partidos_ligas:
            nom_torneo = p["competition"]["name"]
            if nom_torneo not in ligas_agrupadas:
                ligas_agrupadas[nom_torneo] = []
            ligas_agrupadas[nom_torneo].append(p)
            
        for torneo, lista_p in ligas_agrupadas.items():
            st.markdown(f"##### ⚽ {torneo}")
            for partido in lista_p:
                local = partido["homeTeam"]["name"]
                visita = partido["awayTeam"]["name"]
                estado = partido["status"]
                
                if estado in ["IN_PLAY", "PAUSED", "FINISHED"]:
                    marcador = f"**{partido['score']['fullTime']['home']} - {partido['score']['fullTime']['away']}**"
                    badge = "🔴 EN VIVO" if estado != "FINISHED" else "🏁 FIN"
                else:
                    marcador = "vs"
                    badge = f"⏰ {partido['utcDate'].split('T')[1][:5]} UTC"
                
                # Tarjeta limpia para partidos de liga
                with st.container(border=True):
                    c1, c2, c3 = st.columns([3, 2, 3])
                    with c1: st.markdown(f"<p style='text-align: right;'>{local}</p>", unsafe-allow_html=True)
                    with c2: st.markdown(f"<p style='text-align: center;'>{marcador}<br><small>{badge}</small></p>", unsafe-allow_html=True)
                    with c3: st.markdown(f"<p style='text-align: left;'>{visita}</p>", unsafe-allow_html=True)
    else:
        st.info("No hay partidos de ligas europeas registrados para hoy.")


# --- PESTAÑA 3: ENLACES EXTERNOS (PLAN B) ---
with tab_externo:
    st.markdown("¿Querés revisar otras categorías o el minuto a minuto detallado?")
    col1, col2 = st.columns(2)
    with col1:
        st.link_button("🇦🇷 Promiedos", "https://www.promiedos.com.ar", use_container_width=True)
    with col2:
        st.link_button("🌐 Flashscore", "https://www.flashscore.com", use_container_width=True)
