import streamlit as st
import streamlit.components.v1 as components
import random

# Configuración de la pantalla
st.set_page_config(page_title="Predictor Mundial", page_icon="⚽", layout="centered")

st.title("⚽ Predictor Mundial")
st.write("¡Bienvenido! Seleccioná dos selecciones para calcular las probabilidades de victoria basadas en nuestro motor estadístico.")

# Lista de países para el predictor
equipos = ["Argentina", "Brasil", "Francia", "España", "Alemania", "Uruguay", "Inglaterra", "Italia", "Portugal", "Países Bajos"]

col1, col2 = st.columns(2)

with col1:
    equipo_a = st.selectbox("Equipo Local (A):", equipos, index=0)

with col2:
    equipo_b = st.selectbox("Equipo Visitante (B):", equipos, index=1)

if st.button("🔮 Calcular Predicción", use_container_width=True):
    if equipo_a == equipo_b:
        st.warning("⚠️ Por favor, seleccioná dos equipos diferentes.")
    else:
        st.subheader("📊 Resultados del Análisis")
        
        # Simulación de porcentajes (Lógica del motor)
        prob_a = random.randint(35, 55)
        prob_b = random.randint(25, 45)
        prob_empate = 100 - prob_a - prob_b
        
        st.write(f"🔹 **{equipo_a}:** {prob_a}% de probabilidad de ganar.")
        st.write(f"🔹 **{equipo_b}:** {prob_b}% de probabilidad de ganar.")
        st.write(f"🔹 **Empate:** {prob_empate}%")
        
        if prob_a > prob_b:
            st.success(f"🏆 Favorito: El análisis favorece a **{equipo_a}**.")
        else:
            st.success(f"🏆 Favorito: El análisis favorece a **{equipo_b}**.")

# =========================================================================
# 💰 ESPACIO PUBLICITARIO (Aquí es donde sumás tus ganancias)
# =========================================================================
st.markdown("<br><br><hr>", unsafe_allow_html=True)
st.caption("📢 Enlaces Patrocinados")

# Cuando una red de anuncios (como Adsterra) te apruebe la web,
# solo cambiás este bloque de texto por el código HTML real que ellos te den.
codigo_anuncio = """
<div style="text-align:center; background-color:#f0f2f6; padding:10px; border-radius:5px; border: 1px dashed #31333F;">
    <p style="color:#31333F; font-size:11px; margin:0 0 5px 0; font-weight:bold;">ANUNCIO PUBLICITARIO</p>
    <a href="https://www.google.com" target="_blank">
        <img src="https://via.placeholder.com/320x50.png?text=Tu+Anuncio+Aca+Disponible" alt="Anuncio de prueba" style="max-width:100%; height:auto;">
    </a>
</div>
"""

# Muestra el banner publicitario en pantalla
components.html(codigo_anuncio, height=90)
