import streamlit as st
import pandas as pd

# 1. Configuración de Marca Personal
st.set_page_config(
    page_title="Jorge 2.0 | Executive Blueprint",
    page_icon="🧭",
    layout="wide"
)

# Estilo para "Pesar" (Gravedad)
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    div[data-testid="stMetricValue"] { font-size: 2rem; color: #00ffcc; }
    .stCheckbox { margin-bottom: -10px; }
    </style>
    """, unsafe_allow_html=True)

# 2. Sidebar: El Ritual de Control (Checklist Pre-Call)
with st.sidebar:
    st.title("🧘 Ritual de 3s")
    st.write("Antes de desmutearte:")
    st.checkbox("Respiración profunda")
    st.checkbox("Hombros abajo")
    st.checkbox("Tempo lento (Control)")
    
    st.divider()
    st.markdown("### 🛠️ Modo Actual")
    modo = st.select_slider(
        "Tu energía ahora:",
        options=["Fixer", "Architect"],
        value="Architect"
    )
    if modo == "Fixer":
        st.error("⚠️ Estás en modo 'Apagar Incendios'. Frená.")
    else:
        st.success("💎 Estás en modo 'Diseño de Sistemas'.")

# 3. Dashboard Principal
st.title("🧭 Executive Behavioral Blueprint")
st.info("No es motivacional. Es operativo. Es primera división.")

col1, col2, col3 = st.columns(3)
col1.metric("Rol Mental", "Architect", "Fixer")
col2.metric("Comunicación", "Estructural", "Operativa")
col3.metric("Status c/ John", "Estabilizador", "Competitivo")

st.divider()

# 4. El Plan de 30 Días (Interactuable)
st.header("🛠 Plan de Transformación")

tab1, tab2, tab3, tab4 = st.tabs(["Semana 1", "Semana 2", "Semana 3", "Semana 4"])

with tab1:
    st.subheader("🚫 Cero Emocionalidad")
    st.write("Objetivo: Eliminar el ruido, instalar la gravedad.")
    st.checkbox("Cero humor en calls estratégicas", key="s1_1")
    st.checkbox("Cero frases emocionales ('I'm anxious', 'This guy')", key="s1_2")
    st.checkbox("Sustitución de 'I need' por 'The system requires'", key="s1_3")

with tab2:
    st.subheader("📊 Consolidación")
    st.checkbox("Daily por flujo consolidado (End-to-End)", key="s2_1")
    st.checkbox("Aplicar 'Public Sync Rule'", key="s2_2")
    st.checkbox("Enviar resúmenes ejecutivos post-meeting", key="s2_3")

with tab3:
    st.subheader("🏗️ Documentación de Arquitecto")
    st.checkbox("Crear Doc Único de Arquitectura E2E", key="s3_1")
    st.checkbox("Alinear Test Matrix a flujos de negocio", key="s3_2")

with tab4:
    st.subheader("🤫 El Poder del Silencio")
    st.checkbox("Hablar < 20% del tiempo en la reunión", key="s4_1")
    st.checkbox("Hacer solo preguntas de 'Ownership' y 'Blockers'", key="s4_2")

st.divider()

# 5. Manejo de Crisis (Quick Reference)
with st.expander("🔥 Cheat Sheet: Si John entra en pánico..."):
    st.markdown("""
    **Él dice:** *"My confidence is low medium."* **Vos decís:** *"Understood. We’ll drive confidence through flow-based testing and visible ownership."* ---
    **Él dice:** *"We need to push them!"* **Vos decís:** *"What is the specific dependency blocking the closure of this flow?"*
    """)

st.markdown("### *\"El profesional de la hostia no flota. Pesa.\"*")
