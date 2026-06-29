import streamlit as st
import random
import streamlit.components.v1 as components

# Configuración de la pantalla
st.set_page_config(page_title="Predictor Mundial", page_icon="⚽", layout="centered")

# =========================================================================
# 💳 CONTROL DE ACCESO AUTOMÁTICO POR NIVELES (Mercado Pago)
# =========================================================================
parametros = st.query_params

# Inicializamos los estados de suscripción si no existen
if "premium_estandar" not in st.session_state:
    st.session_state["premium_estandar"] = False
if "premium_experto" not in st.session_state:
    st.session_state["premium_experto"] = False

# Leemos qué pase compró el usuario según la URL de retorno
if "status" in parametros and parametros["status"] == "approved":
    tipo_pase = parametros.get("pase", "ninguno")
    if tipo_pase == "estandar":
        st.session_state["premium_estandar"] = True
    elif tipo_pase == "experto":
        st.session_state["premium_estandar"] = True
        st.session_state["premium_experto"] = True

# ⚠️ CONFIGURACIÓN: Pegá acá tus dos links de Mercado Pago
LINK_ESTANDAR = "https://link.mercadopago.com.ar/tu-link-estandar"
LINK_EXPERTO = "https://link.mercadopago.com.ar/tu-link-experto"

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

# PESTAÑA 3: HISTORIAL PREMIUM (Doble Nivel)
elif opcion == "📜 Historial Premium":
    st.title("📜 Centro de Datos Premium")
    
    # CASO 1: Tiene acceso EXPERTO (Ve todo)
    if st.session_state["premium_experto"]:
        st.success("👑 ¡Acceso EXPERTO VIP Verificado!")
        
        tab1, tab2 = st.tabs(["🗂️ Historial General", "🔥 Datos de Oro (Expertos)"])
        
        with tab1:
            st.write("📅 *Hoy* | ⚔️ **Argentina** (52%) vs **Brasil** (38%) | Empate: 10%")
            st.write("📅 *Ayer* | ⚔️ **Francia** (45%) vs **España** (40%) | Empate: 15%")
        
        with tab2:
            st.subheader("💡 Consejos de Simulación Avanzada")
            st.info("📌 **Tendencia:** Argentina mantiene una racha de 5 partidos invicto local. Alta probabilidad de menos de 2.5 goles.")
            st.info("📌 **Alerta de Sorpresa:** Alemania muestra un rendimiento simulado superior al 60% frente a rivales europeos este mes.")

    # CASO 2: Tiene acceso ESTÁNDAR (Ve solo el historial)
    elif st.session_state["premium_estandar"]:
        st.success("🔓 ¡Acceso Estándar Verificado!")
        st.subheader("🗂️ Registro de Predicciones Recientes")
        st.write("📅 *Hoy* | ⚔️ **Argentina** (52%) vs **Brasil** (38%) | Empate: 10%")
        st.write("📅 *Ayer* | ⚔️ **Francia** (45%) vs **España** (40%) | Empate: 15%")
        
        st.markdown("---")
        st.warning("⭐ ¿Querés los consejos de apuestas del Pase Experto?")
        st.link_button("🚀 Subir a Pase Experto", LINK_EXPERTO, use_container_width=True)

    # CASO 3: No pagó nada todavía (Muro de pago doble)
    else:
        st.error("🔒 Sección Exclusiva")
        st.write("Elegí el plan que mejor se adapte a tu estilo de juego para desbloquear las herramientas estadísticas:")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### 🥉 Pase Estándar\n**$2.990** (Único)")
            st.write("✅ Historial completo de partidos.")
            st.write("✅ Registro de porcentajes.")
            st.link_button("💳 Comprar Estándar", LINK_ESTANDAR, use_container_width=True)
            
        with col2:
            st.markdown("### 🥇 Pase Experto\n**$6.990** (Único)")
            st.write("✅ Todo lo del pase Estándar.")
            st.write("🔥 **Consejos de apuestas y rachas.**")
            st.write("🔥 **Alertas de partidos sorpresa.**")
            st.link_button("⚡ ¡Comprar Experto!", LINK_EXPERTO, type="primary", use_container_width=True)
