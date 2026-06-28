import streamlit as st
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
