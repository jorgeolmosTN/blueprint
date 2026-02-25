import streamlit as st
import pandas as pd
from datetime import datetime

# Configuración de la página
st.set_page_config(page_title="Executive Blueprint 2.0", page_icon="🧭", layout="wide")

# Estilo personalizado para dar "Gravedad"
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stMetric { background-color: #ffffff; padding: 15px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    .executive-card { padding: 20px; border-left: 5px solid #1E3A8A; background-color: white; margin-bottom: 10px; border-radius: 5px; }
    </style>
    """, unsafe_allow_html=True)

# Sidebar - El Ritual
with st.sidebar:
    st.title("🧘 Ritual de Control")
    st.info("Antes de cada call:")
    st.checkbox("Respirar profundo")
    st.checkbox("Bajar hombros")
    st.checkbox("Hablar más lento (Tempo Ejecutivo)")
    
    st.divider()
    st.write("### 🗣️ Sustitución de Energía")
    mode = st.radio("Modo actual:", ["Fixer (Operativo)", "Architect (Estratégico)"])
    if mode == "Fixer (Operativo)":
        st.warning("⚠️ Cuidado: Estás resolviendo, no estructurando.")
    else:
        st.success("✅ Estás diseñando sistemas.")

# Header
st.title("🧭 Executive Behavioral Blueprint – Jorge 2.0")
st.caption("De 'Fixer' a 'Architect of Execution' | Enfoque: Estructura y Gravedad")

---

# I. Diagnóstico y Mindset
col1, col2 = st.columns(2)

with col1:
    st.subheader("🧠 El Cambio de Identidad")
    st.markdown("""
    <div class="executive-card">
        <h4>Fixer ➔ Architect</h4>
        <p><i>"Yo no soluciono. Yo estructuro."</i></p>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("**Preguntas Estructurales:**")
    st.code("¿Quién es el owner de definir eso?\n¿Qué te está bloqueando?\n¿Qué cambió desde el compromiso?")

with col2:
    st.subheader("🗣️ Diccionario Ejecutivo")
    data = {
        "Prohibido (Energía Operativa)": ["This guy...", "I'm anxious about...", "It's impossible"],
        "Ejecutivo (Liderazgo Estructural)": ["That dependency is unresolved.", "Let's define ownership.", "We need architectural confirmation."]
    }
    st.table(pd.DataFrame(data))

---

# II. Gestión Estratégica (The John Factor)
st.subheader("🔥 Manejo de Stakeholders de Alta Intensidad")
with st.expander("Ver protocolo para John / Ansiedad Estratégica"):
    st.write("""
    **Situación:** John dice "My confidence is low medium".
    
    **Tu respuesta (Estabilizador):**
    > "Understood. We’ll drive confidence through flow-based testing and visible ownership."
    """)
    st.progress(100, text="Objetivo: Estabilizar, no competir en energía.")

---

# III. Plan de 30 Días (Tracker)
st.subheader("🛠 Plan de Transformación de la Hostia")

tabs = st.tabs(["Semana 1", "Semana 2", "Semana 3", "Semana 4"])

with tabs[0]:
    st.write("### 🚫 Cero Emocionalidad")
    st.checkbox("Cero humor en calls estratégicas")
    st.checkbox("Cero frases emocionales")
    st.checkbox("Uso exclusivo de lenguaje estructural")

with tabs[1]:
    st.write("### 📊 Consolidación")
    st.checkbox("Daily por flujo consolidado")
    st.checkbox("Public sync rule aplicada")
    st.checkbox("Resúmenes ejecutivos post-meeting")

with tabs[2]:
    st.write("### 🏗️ Arquitectura")
    st.checkbox("Documento único de end-to-end architecture")
    st.checkbox("Test matrix alineada a flows")

with tabs[3]:
    st.write("### 🤫 El Poder del Silencio")
    st.checkbox("Hablar menos en reuniones")
    st.checkbox("Hacer solo preguntas estructurales")

---

# IV. Closure
st.divider()
st.markdown("""
<div style="text-align: center;">
    <h3>"El profesional de la hostia no flota. Pesa."</h3>
    <p>Gravedad confirmada.</p>
</div>
""", unsafe_allow_html=True)