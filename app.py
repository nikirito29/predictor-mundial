import streamlit as st
import random
import streamlit.components.v1 as components

# Configuración de la pantalla
st.set_page_config(page_title="Predictor Mundial", page_icon="⚽", layout="centered")

# =========================================================================
# 💳 CONTROL DE ACCESO AUTOMÁTICO POR SUSCRIPCIÓN
# =========================================================================
parametros = st.query_params

if "premium_estandar" not in st.session_state:
    st.session_state["premium_estandar"] = False
if "premium_experto" not in st.session_state:
    st.session_state["premium_experto"] = False

# Verificamos la suscripción activa según la URL de retorno de Mercado Pago
if "status" in parametros and parametros["status"] == "approved":
    tipo_suscripcion = parametros.get("plan", "ninguno")
    if tipo_suscripcion == "mensual_estandar":
    LINK_SUSCRIPCION_ESTANDAR = "https://www.mercadopago.com.ar/subscriptions/TU_LINK_REAL_ACA"
LINK_SUSCRIPCION_EXPERTO = "https://www.mercadopago.com.ar/subscriptions/TU_LINK_REAL_ACA"
    elif tipo_suscripcion == "mensual_experto":
        st.session_state["premium_estandar"] = True
        st.session_state["premium_experto"] = True

# ⚠️ CONFIGURACIÓN: Pegá acá tus dos links de SUSCRIPCIÓN de Mercado Pago
LINK_SUSCRIPCION_ESTANDAR = "https://www.mercadopago.com.ar/subscriptions/tu-link-suscripcion-estandar"
LINK_SUSCRIPCION_EXPERTO = "https://www.mercadopago.com.ar/subscriptions/tu-link-suscripcion-experto"
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

# PESTAÑA 1: PREDICTOR
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

# PESTAÑA 2: PARTIDOS EN VIVO
elif opcion == "📺 Partidos en Vivo":
    st.title("📺 Marcador en Directo")
    st.write("Seguí los resultados del fútbol mundial en tiempo real.")
    
    html_marcador = """
    <iframe src="https://www.scoreaxis.com/widget/live-match-center?autoHeight=1&amp;bodyBackground=%231a1a1a&amp;textColor=%23ffffff" 
            width="100%" height="600" style="border:none;" id="scoreaxis-widget">
    </iframe>
    """
    components.html(html_marcador, height=650, scrolling=True)

# PESTAÑA 3: HISTORIAL PREMIUM
elif opcion == "📜 Historial Premium":
    st.title("📜 Centro de Datos Premium")
    
    if st.session_state["premium_experto"]:
        st.success("👑 ¡Suscripción EXPERTO VIP Activa!")
        tab1, tab2 = st.tabs(["🗂️ Historial General", "🔥 Datos de Oro (Expertos)"])
        with tab1:
            st.write("📅 *Hoy* | ⚔️ **Argentina** (52%) vs **Brasil** (38%) | Empate: 10%")
        with tab2:
            st.subheader("💡 Consejos de Simulación Avanzada")
            st.info("📌 **Tendencia:** Alta probabilidad de menos de 2.5 goles en el próximo partido.")

    elif st.session_state["premium_estandar"]:
        st.success("🔓 ¡Suscripción Estándar Activa!")
        st.subheader("🗂️ Registro de Predicciones Recientes")
        st.write("📅 *Hoy* | ⚔️ **Argentina** (52%) vs **Brasil** (38%) | Empate: 10%")
        st.markdown("---")
        st.warning("⭐ ¿Querés los consejos de apuestas del Plan Experto?")
        st.link_button("🚀 Subir a Plan Experto", LINK_SUSCRIPCION_EXPERTO, use_container_width=True)

    else:
        st.error("🔒 Sección Exclusiva por Suscripción")
        st.write("Suscribite mensualmente para desbloquear las mejores herramientas estadísticas de fútbol. Podés cancelar cuando quieras.")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### 🥉 Plan Estándar\n**$1.490 / mes**")
            st.write("✅ Historial completo de partidos.")
            st.link_button("💳 Suscribirme Estándar", LINK_SUSCRIPCION_ESTANDAR, use_container_width=True)
            
        with col2:
            st.markdown("### 🥇 Plan Experto\n**$2.990 / mes**")
            st.write("✅ Todo lo del plan Estándar.")
            st.write("🔥 **Consejos de apuestas y alertas.**")
            st.link_button("⚡ ¡Suscribirme Experto!", LINK_SUSCRIPCION_EXPERTO, type="primary", use_container_width=True)
    
