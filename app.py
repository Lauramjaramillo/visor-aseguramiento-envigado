import streamlit as st
from typing import Callable, Optional, Dict
from src.config import MENU_STRUCTURE, TEXTO_BIENVENIDA
from src.components.sidebar import render_sidebar
from src.views.visor_web import render_iframe
from src.views.directorio import render_directorio

# Configuración inicial de la página
st.set_page_config(
    page_title="Visor Aseguramiento - Envigado",
    page_icon="🍊",
    layout="wide",
    initial_sidebar_state="expanded"
)

def obtener_url_seleccionada(seleccion: str) -> Optional[str]:
    """Busca la URL asociada a una selección dentro de la estructura de grupos."""
    for categoria, detalles in MENU_STRUCTURE.items():
        if detalles.get("type") == "group" and seleccion in detalles.get("items", {}):
            return detalles["items"][seleccion]
    return None

def main() -> None:
    """
    Función principal que actúa como despachador (dispatcher) de vistas.
    Gestiona la navegación y el renderizado de componentes según la selección.
    """
    seleccion = render_sidebar()
    
    # Mapa de despacho: asocia selecciones con funciones de renderizado
    # Permite escalar sin añadir nuevos bloques if/else
    vistas: Dict[str, Callable] = {
        "Inicio": lambda: (
            st.title("Sistema de Consolidación y Consulta"), 
            st.markdown(TEXTO_BIENVENIDA),
            st.info("👈 Utilice el menú lateral o la barra de búsqueda para acceder a los reportes y bases de datos externas.")
        ),
        "Directorio de Consultas": render_directorio
    }

    try:
        if seleccion in vistas:
            vistas[seleccion]()
        else:
            # Lógica para reportes dinámicos
            url_destino = obtener_url_seleccionada(seleccion)
            if url_destino:
                render_iframe(titulo=seleccion, url=url_destino)
            else:
                st.error(f"Error: No se encontró un recurso asociado a '{seleccion}'.")
                
    except Exception as error:
        st.error("Ocurrió un error inesperado al cargar la vista.")
        st.exception(error)

if __name__ == "__main__":
    main()