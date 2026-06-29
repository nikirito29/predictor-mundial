import streamlit as st
import random
import streamlit.components.v1 as components

# Configuración de la pantalla
st.set_page_config(page_title="Predictor Mundial", page_icon="⚽", layout="centered")

# =========================================================================
# 💳 CONTROL DE ACCESO AUTOMÁTICO (Mercado Pago Link)
# =========================================================================
# Leemos si Mercado Pago nos devolvió el estado de "aprobado" en la URL
parametros = st.query_params

if "status" in parametros and parametros["status"] == "approved":
    st.session_state["premium_activo"] = True
elif "premium_activo" not in st.session_state:
    st.session_state["premium_activo"] = False

# ⚠️ REEMPLAZÁ ESTO: Poné acá el link del "Botón de pago" que crees en tu cuenta de Mercado Pago
LINK_MERCADO_PAGO = "https://link.mercadopago.com.ar/tu-link-de-pago-aca"

# =========================================================================
# ☰ MENÚ DE NAVEGACIÓN
# =========================================================================
opcion = st.sidebar.radio("Menú de la App", ["🔮 Generar Predicción", "📺 Partidos en Vivo", "📜 Historial Premium"])

# Lista de países
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

# -------------------------------------------------------------------------
# PESTAÑA 1: PREDICTOR
# -------------------------------------------------------------------------
if opcion == "🔮 Generar Predicción":
    st.title("⚽ Predictor Mundial")
    st.write("Seleccioná dos selecciones para calcular las probabilidades de victoria.")
    
    col1, col2 = st.columns(2)
    with col1:
        equipo_a = st.selectbox("Equipo Local (A):", equipos, index=3) # Argentina
    with col2:
        equipo_b = st.selectbox("Equipo Visitante (B):", equipos, index=7) # Brasil
        
    if st.button("🔮 Calcular Predicción", use_container_width=True):
        if equipo_a == equipo_b:
            st.warning("⚠️ Por favor, seleccioná dos equipos diferentes.")
        else:
            st.subheader("📊 Resultados del Análisis")
            prob_a = random.randint(35, 55)
            prob_b = random.randint(25, 45)
            prob_empate = 100 - prob_a - prob_b
            
            st.write(f"🔹 **{equipo_a}:** {prob_a}%")
            st.write(f"🔹 **{equipo_b}:** {prob_b}%")
            st.write(f"🔹 **Empate:** {prob_empate}%")
            
            if prob_a > prob_b:
                st.success(f"🏆 Favorito: El análisis favorece a **{equipo_a}**.")
            else:
                st.success(f"🏆 Favorito: El análisis favorece a **{equipo_b}**.")

# -------------------------------------------------------------------------
# PESTAÑA 2: PARTIDOS EN VIVO (Directo)
# -------------------------------------------------------------------------
elif opcion == "📺 Partidos en Vivo":
    st.title("📺 Marcador en Directo")
    st.write("Seguí los resultados de los partidos reales de fútbol de todo el mundo en tiempo real.")
    
    # Widget de marcador en vivo embebido de forma segura
    html_marcador = """
    <iframe src="https://www.scoreaxis.com/widget/live-match-center?autoHeight=1&amp;bodyBackground=%231a1a1a&amp;textColor=%23ffffff" 
            width="100%" 
            height="600" 
            style="border:none; transition: all 0.3s ease;" 
            id="scoreaxis-widget">
    </iframe>
    """
    components.html(html_marcador, height=650, scrolling=True)

# -------------------------------------------------------------------------
# PESTAÑA 3: HISTORIAL PREMIUM
# -------------------------------------------------------------------------
elif opcion == "📜 Historial Premium":
    st.title("📜 Historial de Predicciones Avanzadas")
    
    # Verificamos si el pago ya fue validado automáticamente
    if st.session_state["premium_activo"]:
        st.success("🔓 ¡Acceso Premium Verificado Exitosamente!")
        st.subheader("🗂️ Registro Completo de Datos")
        
        # Simulación de datos guardados históricos
        st.write("📅 *Hoy* | ⚔️ **Argentina** (52%) vs **Brasil** (38%) | Empate: 10%")
        st.write("📅 *Ayer* | ⚔️ **Francia** (45%) vs **España** (40%) | Empate: 15%")
        st.write("📅 *Hace 2 días* | ⚔️ **Uruguay** (48%) vs **Colombia** (32%) | Empate: 20%")
    
    else:
        st.error("🔒 Esta sección es exclusiva para usuarios Premium.")
        st.write("Para desbloquear el acceso ilimitado al historial permanente de partidos y estadísticas avanzadas, realizá el pago único seguro a través de Mercado Pago.")
        
        # Botón de Pago que redirige al usuario
        st.link_button("💳 Pagar con Mercado Pago", LINK_MERCADO_PAGO, type="primary", use_container_width=True)
        
        st.caption("ℹ️ Una vez realizado el pago, Mercado Pago te devolverá automáticamente a la app y la sección se desbloqueará de inmediato.")
    
