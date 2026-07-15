import streamlit as st
from src.config import ENLACES_EXTERNOS

def render_directorio():
    st.markdown("<h2 style='color: #EA5B0C;'>🌐 Directorio de Consultas</h2>", unsafe_allow_html=True)
    st.markdown("---")
    
    for categoria, enlaces in ENLACES_EXTERNOS.items():
        st.subheader(categoria)
        cols = st.columns(2) # Dos tarjetas por fila
        for i, enlace in enumerate(enlaces):
            with cols[i % 2]:
                with st.container(border=True):
                    st.markdown(f"#### {enlace['nombre']}")
                    st.caption(enlace['desc'])
                    st.link_button("Ir al portal ↗", enlace['url'], use_container_width=True)