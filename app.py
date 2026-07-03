import streamlit as st
import requests

# 🧠 1. MEMORIA DE LA APP: Inicializamos la variable para abrir/cerrar el formulario
if "mostrar_formulario" not in st.session_state:
    st.session_state.mostrar_formulario = False

# Configuración inicial de estilo móvil
st.markdown("""
    <style>
    .block-container { padding-top: 2rem; padding-bottom: 2rem; }
    </style>
""", unsafe_allow_html=True)

# --- 2. BANNER DESTACADO (Arriba de todo) ---
st.markdown("### 🔥 Partido Destacado de Hoy")
with st.container(border=True):
    col_A, col_B = st.columns([2, 1])
    with col_A:
        st.markdown("🇦🇷 **Argentina vs. Cabo Verde**")
        st.caption("🏆 Fase de Grupos • ¡Pronósticos abiertos!")
    with col_B:
        # Al tocar el botón, cambia el estado entre Verdadero y Falso
        if st.button("🎯 Predecir", key="btn_destacado", use_container_width=True):
            st.session_state.mostrar_formulario = not st.session_state.mostrar_formulario

# 🔮 FORMULARIO INTERACTIVO: Si el usuario tocó "Predecir", se despliega esto abajo
if st.session_state.mostrar_formulario:
    with st.container(border=True):
        st.markdown("#### 🔮 Ingresá tu Pronóstico Exacto")
        col_g1, col_g2 = st.columns(2)
        with col_g1:
            goles_local = st.number_input("Goles Argentina", min_value=0, max_value=15, value=1, step=1, key="g_local_p")
        with col_g2:
            goles_visita = st.number_input("Goles Cabo Verde", min_value=0, max_value=15, value=0, step=1, key="g_visita_p")
        
        # Botón final dentro del formulario para confirmar el resultado
        if st.button("Confirmar Pronóstico", type="primary", use_container_width=True):
            st.success(f"¡Pronóstico enviado! Guardaste: **Argentina {goles_local} - {goles_visita} Cabo Verde** 🚀")
            st.balloons() # ¡Tira globos de festejo en toda la pantalla!
            st.session_state.mostrar_formulario = False # Cierra el panel automáticamente


st.write("") # Espacio visual

# --- 3. SECCIONES POR PESTAÑAS ---
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

todos_los_partidos = obtener_partidos()


# --- PESTAÑA 1: MUNDIAL ---
with tab_mundial:
    partidos_wc = [p for p in todos_los_partidos if p.get("competition", {}).get("code") == "WC"]
    
    if partidos_wc:
        for partido in partidos_wc:
            local = partido["homeTeam"]["name"]
            visita = partido["awayTeam"]["name"]
            estado = partido["status"]
            
            if estado in ["IN_PLAY", "PAUSED", "FINISHED"]:
                g_local = partido["score"]["fullTime"]["home"]
                g_visita = partido["score"]["fullTime"]["away"]
                marcador = f"**{g_local} - {g_visita}**"
                badge = "🔴 EN VIVO" if estado != "FINISHED" else "🏁 FIN"
            else:
                marcador = "vs"
                badge = f"⏰ {partido['utcDate'].split('T')[1][:5]} UTC"

            with st.container(border=True):
                c1, c2, c3 = st.columns([3, 2, 3])
                with c1: st.markdown(f"<p style='text-align: right;'><b>{local}</b></p>", unsafe_allow_html=True)
                with c2: st.markdown(f"<p style='text-align: center;'>{marcador}<br><small>{badge}</small></p>", unsafe_allow_html=True)
                with c3: st.markdown(f"<p style='text-align: left;'><b>{visita}</b></p>", unsafe_allow_html=True)
    else:
        st.info("No hay partidos del Mundial programados para hoy en la API.")


# --- PESTAÑA 2: LIGAS EUROPEAS ---
with tab_ligas:
    partidos_ligas = [p for p in todos_los_partidos if p.get("competition", {}).get("code") != "WC"]
    
    if partidos_ligas:
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
                
                with st.container(border=True):
                    c1, c2, c3 = st.columns([3, 2, 3])
                    with c1: st.markdown(f"<p style='text-align: right;'>{local}</p>", unsafe_allow_html=True)
                    with c2: st.markdown(f"<p style='text-align: center;'>{marcador}<br><small>{badge}</small></p>", unsafe_allow_html=True)
                    with c3: st.markdown(f"<p style='text-align: left;'>{visita}</p>", unsafe_allow_html=True)
    else:
        st.info("No hay partidos de ligas europeas registrados para hoy.")


# --- PESTAÑA 3: ENLACES EXTERNOS ---
with tab_externo:
    st.markdown("¿Querés revisar otras categorías o el minuto a minuto detallado?")
    col1, col2 = st.columns(2)
    with col1:
        st.link_button("🇦🇷 Promiedos", "https://www.promiedos.com.ar", use_container_width=True)
    with col2:
        st.link_button("🌐 Flashscore", "https://www.flashscore.com", use_container_width=True)
                
