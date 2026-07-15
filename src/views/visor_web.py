import streamlit as st
import streamlit.components.v1 as components

def render_iframe(titulo: str, url: str):
    """
    Renderiza el iframe optimizando el espacio en pantalla al máximo
    e informando al usuario sobre políticas de seguridad externas.
    """
    if not url:
        st.warning("La URL para este reporte aún no está configurada.")
        return

    # AUMENTAMOS LA PROPORCIÓN DE LA COLUMNA 2
    # Cambiamos [3, 1] por [2, 1] para darle más ancho al botón
    col1, col2 = st.columns([2, 1], vertical_alignment="bottom")

    with col1:
        st.subheader(titulo)

    with col2:
        st.link_button("↗ Abrir en ventana externa", url, type="primary", use_container_width=True)

    st.caption("💡 **Nota de seguridad:** Si el recuadro inferior aparece en gris, significa que la entidad origen bloquea la visualización incrustada. Por favor, utilice el botón naranja superior para consultar.")
    
    with st.spinner("Cargando información..."):
        components.iframe(url, height=1000, scrolling=True)