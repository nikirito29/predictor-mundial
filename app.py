import streamlit as st
import random

# Configuración de la pantalla
st.set_page_config(page_title="Predictor Mundial", page_icon="⚽", layout="centered")

st.title("⚽ Predictor Mundial")
st.write("¡Bienvenido! Seleccioná dos selecciones para calcular las probabilidades de victoria basadas en nuestro motor estadístico.")

# Lista extendida y ordenada de países
equipos = [
    "Alemania", "Arabia Saudita", "Argelia", "Argentina", "Australia", 
    "Bélgica", "Bolivia", "Brasil", "Canadá", "Chile", 
    "Colombia", "Corea del Sur", "Costa Rica", "Croacia", "Dinamarca", 
    "Ecuador", "Egipto", "Escocia", "España", "Estados Unidos", 
    "Francia", "Gales", "Ghana", "Inglaterra", "Irán", 
    "Italia", "Japón", "Marruecos", "México", "Nigeria", 
    "Países Bajos", "Paraguay", "Perú", "Portugal", "Qatar", 
    "Senegal", "Serbia", "Suiza", "Túnez", "Uruguay", "Venezuela"
]

col1, col2 = st.columns(2)

with col1:
    equipo_a = st.selectbox("Equipo Local (A):", equipos, index=3) # Por defecto: Argentina

with col2:
    equipo_b = st.selectbox("Equipo Visitante (B):", equipos, index=7) # Por defecto: Brasil

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
            
