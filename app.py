import streamlit as st
from src.config import MENU_STRUCTURE, TEXTO_BIENVENIDA
from src.components.sidebar import render_sidebar
from src.views.visor_web import render_iframe
from src.views.directorio import render_directorio  # NUEVO: Importamos el directorio

st.set_page_config(
    page_title="Visor Aseguramiento - Envigado",
    page_icon="🍊",
    layout="wide",
    initial_sidebar_state="expanded"
)

def obtener_url_seleccionada(seleccion):
    # Buscamos en los grupos para encontrar URLs de Power BI
    for categoria, detalles in MENU_STRUCTURE.items():
        if detalles.get("type") == "group" and seleccion in detalles.get("items", {}):
            return detalles["items"][seleccion]
    return None

def main():
    # 1. Obtenemos la selección del menú lateral
    seleccion = render_sidebar()
    
    # 2. Enrutamiento Principal
    if seleccion == "Inicio":
        st.title("Sistema de Consolidación y Consulta")
        st.markdown(TEXTO_BIENVENIDA)
        st.info("👈 Utilice el menú lateral o la barra de búsqueda para acceder a los reportes y bases de datos externas.")
        
    elif seleccion == "Directorio de Consultas":
        # NUEVO: Si el usuario selecciona el Hub, renderizamos el directorio
        render_directorio()
        
    else:
        # 3. Lógica para reportes de Power BI
        url_destino = obtener_url_seleccionada(seleccion)
        
        if url_destino:
            render_iframe(titulo=seleccion, url=url_destino)
        else:
            # Manejo de error si la selección no tiene URL
            st.title(seleccion)
            st.error("No se encontró un reporte asociado a esta selección.")

if __name__ == "__main__":
    main()