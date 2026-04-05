"""
=============================================================================
  Extractor de Formularios DIAN → Excel - LANDING PAGE
=============================================================================
"""

import streamlit as st

st.set_page_config(
    page_title="Extractor DIAN - Inicio",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
    
    .main-header {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
        padding: 3rem 2.5rem;
        border-radius: 16px;
        margin-bottom: 2rem;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
        border: 1px solid rgba(255, 255, 255, 0.05);
        text-align: center;
    }
    .main-header h1 { color: #e2e8f0; font-size: 3rem; font-weight: 700; margin: 0; }
    .main-header p { color: #94a3b8; font-size: 1.2rem; margin-top: 1rem; }
    .main-header .accent {
        background: linear-gradient(90deg, #60a5fa, #a78bfa);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    }

    .card {
        background: linear-gradient(145deg, #1e293b, #0f172a);
        padding: 2rem; border-radius: 12px;
        border: 1px solid rgba(99, 102, 241, 0.2);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
        height: 100%;
    }
    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 24px rgba(99, 102, 241, 0.15);
    }
    .card h2 { color: #e2e8f0; font-size: 1.8rem; margin-top: 0; }
    .card p { color: #94a3b8; font-size: 1rem; line-height: 1.6; }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="main-header">
    <h1>📊 Plataforma <span class="accent">DIAN</span> Automator</h1>
    <p>Centraliza y consolida la información de tus declaraciones tributarias en segundos.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style="background: rgba(99, 102, 241, 0.05); padding: 2rem; border-radius: 12px; margin-bottom: 2.5rem; border-left: 4px solid #60a5fa;">
    <h3 style="margin-top: 0;">💡 ¿Cómo funciona?</h3>
    <ol style="color: #cbd5e1; font-size: 1.1rem; line-height: 1.8; margin-bottom: 0;">
        <li><strong>Selecciona tu formulario:</strong> Haz clic en el panel inferior o en la barra lateral para abrir el módulo del Formulario 300 o 350.</li>
        <li><strong>Carga tus archivos:</strong> Arrastra y suelta todos los PDFs de tus declaraciones. El algoritmo leerá inteligentemente los meses y extraerá casilla por casilla.</li>
        <li><strong>Descarga y consolida:</strong> Revisa la consistencia de los datos en pantalla y pulsa "Descargar Excel" para obtener una sábana financiera con todos tus periodos.</li>
    </ol>
</div>
""", unsafe_allow_html=True)

st.markdown("### 📌 Selecciona el módulo de extracción:")
st.markdown("<br>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="card">
        <h2>📝 Formulario 300 (IVA)</h2>
        <p>Extrae casillas precisas del formulario de <strong>Declaración de Impuesto sobre las Ventas</strong>, organizadas en columnas por periodo para una fácil comparativa.</p>
        <p style="color: #6ee7b7;">✓ Soporte BIMESTRAL y CUATRIMESTRAL</p>
        <br>
    </div>
    """, unsafe_allow_html=True)
    try:
        st.page_link("pages/1_Formulario_300.py", label="Abrir Módulo 300 »", icon="📝")
    except AttributeError:
        st.info("👈 Selecciona '1 Formulario 300' en el menú lateral de la izquierda")

with col2:
    st.markdown("""
    <div class="card">
        <h2>🏢 Formulario 350 (Retención)</h2>
        <p>Procesa múltiples PDFs separando automáticamente las bases y retenciones de <strong>Personas Jurídicas</strong> y <strong>Naturales</strong> en un formato estructurado.</p>
        <p style="color: #6ee7b7;">✓ Estructuración MultiIndex Dinámica</p>
        <p style="color: #6ee7b7;">✓ Nueva extracción precisa de 12 meses</p>
    </div>
    """, unsafe_allow_html=True)
    try:
        st.page_link("pages/2_Formulario_350.py", label="Abrir Módulo 350 »", icon="🏢")
    except AttributeError:
        st.info("👈 Selecciona '2 Formulario 350' en el menú lateral de la izquierda")

st.markdown("<br><br><br><hr>", unsafe_allow_html=True)
st.markdown("### 📈 Ejemplo del Entregable")
st.markdown("<p style='color:#cbd5e1'>Al procesar tus archivos con éxito, la plataforma generará automáticamente un documento <strong>Excel Profesional</strong> listo para su análisis financiero, estructurado visualmente como el siguiente ejemplo:</p>", unsafe_allow_html=True)

try:
    st.image("assets/excel_example.png", use_container_width=True)
except Exception:
    pass

st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<center><small>Desarrollado para agilizar la gestión tributaria y auditoría contable.</small></center>", unsafe_allow_html=True)
