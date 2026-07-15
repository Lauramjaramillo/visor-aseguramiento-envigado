import streamlit as st
from typing import Callable, Optional, Dict
from src.config import MENU_STRUCTURE, TEXTO_BIENVENIDA
from src.components.sidebar import render_sidebar
from src.views.visor_web import render_iframe
from src.views.directorio import render_directorio

# Configuración inicial de la página
st.set_page_config(
    page_title="Portal Gestión del Aseguramiento - Envigado",
    page_icon="⚕️",
    layout="wide",
    initial_sidebar_state="expanded"
)

def obtener_url_seleccionada(seleccion: str) -> Optional[str]:
    """
    Busca la URL asociada a una selección de menú dentro de la estructura de grupos.

    Args:
        seleccion (str): Nombre del elemento seleccionado en el sidebar.

    Returns:
        Optional[str]: La URL del recurso si existe, de lo contrario None.
    """
    for categoria, detalles in MENU_STRUCTURE.items():
        if detalles.get("type") == "group" and seleccion in detalles.get("items", {}):
            return detalles["items"][seleccion]
    return None

def main() -> None:
    """
    Función principal (Entry Point).
    
    Actúa como el despachador (dispatcher) central de la aplicación. Gestiona la 
    navegación, invoca el renderizado de la vista correspondiente y encapsula 
    el manejo de errores global para garantizar la estabilidad del portal.
    """
    seleccion = render_sidebar()
    
    # Mapa de despacho: asocia selecciones con funciones de renderizado
    vistas: Dict[str, Callable] = {
        "Inicio": lambda: (
            st.image("assets/escudo_envigado.png", width=150),
            # st.title eliminado para evitar duplicidad
            st.markdown(TEXTO_BIENVENIDA),
            st.info("👈 Utilice el menú lateral o la barra de búsqueda para acceder a los reportes y bases de datos externas.")
        ),
        "Directorio de Consultas": render_directorio
    }

    try:
        # Enrutamiento basado en el mapa de despacho
        if seleccion in vistas:
            vistas[seleccion]()
        else:
            # Lógica para reportes dinámicos de Power BI
            url_destino = obtener_url_seleccionada(seleccion)
            if url_destino:
                render_iframe(titulo=seleccion, url=url_destino)
            else:
                st.error(f"Error: No se encontró un recurso asociado a '{seleccion}'.")
        
        # Pie de página institucional uniforme
        st.markdown("---")
        st.markdown(
            "<div style='text-align: center; color: gray; font-size: 0.8em;'>"
            "© 2026 - Municipio de Envigado | Dirección de Aseguramiento"
            "</div>", 
            unsafe_allow_html=True
        )
                
    except Exception as error:
        st.error("Ocurrió un error inesperado al cargar la vista.")
        st.exception(error)

if __name__ == "__main__":
    main()