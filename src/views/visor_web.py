import streamlit as st
import streamlit.components.v1 as components
from typing import Optional

def render_iframe(titulo: str, url: str) -> None:
    """
    Renderiza un componente iframe encapsulado para visualización de reportes externos.

    Incluye una capa de seguridad básica para validar la URL y una interfaz 
    de usuario optimizada para maximizar el área de trabajo del reporte.

    Args:
        titulo (str): Título que se mostrará sobre el reporte.
        url (str): Dirección web del recurso a incrustar.
    
    Raises:
        Exception: Captura errores durante la inicialización del componente iframe.
    """
    if not url or not url.startswith("http"):
        st.error("URL no válida o no configurada.")
        return

    try:
        # Layout optimizado para uso de pantalla
        col1, col2 = st.columns([2, 1], vertical_alignment="bottom")

        with col1:
            st.subheader(titulo)

        with col2:
            st.link_button(
                "↗ Abrir en ventana externa", 
                url, 
                type="primary", 
                use_container_width=True
            )

        st.info(
            "💡 **Nota de seguridad:** Si el recuadro inferior aparece en gris, "
            "la entidad de origen restringe la visualización externa. Use el "
            "botón superior para consultar en una nueva pestaña."
        )
        
        # Renderizado del componente con manejo de carga
        with st.container():
            components.iframe(
                src=url, 
                height=1000, 
                scrolling=True
            )
            
    except Exception as error:
        st.error(f"Error al intentar cargar el reporte: {titulo}")
        st.exception(error)

if __name__ == "__main__":
    # Test rápido de componente
    render_iframe("Reporte de Prueba", "https://www.google.com")