import streamlit as st
from src.config import ENLACES_EXTERNOS

def render_directorio():
    """
    Renderiza la vista del Directorio de Consultas organizando los enlaces externos
    por categorías en un diseño de tarjetas responsivo.

    Maneja excepciones de forma individual para cada bloque de enlaces, asegurando
    que un fallo en la estructura de una categoría no afecte la renderización del resto.
    """
    try:
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
                        
    except Exception as e:
        st.error("Ocurrió un error al cargar el directorio de consultas.")
        st.exception(e)