import streamlit as st
import pandas as pd
from motor import procesar_datos_y_entrenar, predecir

st.set_page_config(page_title="Predictor Mundial", page_icon="⚽")
st.title("🏆 Predictor Mundial de Fútbol")

@st.cache_resource
def iniciar_sistema():
    return procesar_datos_y_entrenar()

modelo, conn = iniciar_sistema()

equipos_df = pd.read_sql_query("SELECT nombre FROM equipos ORDER BY nombre", conn)
lista_equipos = equipos_df['nombre'].tolist()

col1, col2 = st.columns(2)
with col1:
    equipo_local = st.selectbox("Equipo Local", lista_equipos, index=0)
with col2:
    indice_visita = 1 if len(lista_equipos) > 1 else 0
    equipo_visitante = st.selectbox("Equipo Visitante", lista_equipos, index=indice_visita)

if st.button("⚽ Predecir Resultado", type="primary"):
    if equipo_local == equipo_visitante:
        st.warning("⚠️ Selecciona dos equipos diferentes.")
    else:
        probabilidad, elo_l, elo_v = predecir(modelo, conn, equipo_local, equipo_visitante)
        st.write(f"**Puntuación ELO:** {equipo_local} ({elo_l:.0f}) vs {equipo_visitante} ({elo_v:.0f})")
        st.success(f"📈 Probabilidad de victoria para **{equipo_local}**: {probabilidad:.2%}")
        st.info(f"📉 Probabilidad de empate o victoria para **{equipo_visitante}**: {1 - probabilidad:.2%}")
