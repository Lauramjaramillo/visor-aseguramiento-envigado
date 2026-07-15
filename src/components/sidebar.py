import streamlit as st
from typing import Dict, Any
from src.config import MENU_STRUCTURE

# Constantes para evitar errores de tipo "Magic Strings"
KEY_PAGINA_ACTUAL = "pagina_actual"
TIPO_GROUP = "group"
TIPO_PAGE = "page"
LABEL_INICIO = "Inicio"

def render_sidebar() -> str:
    """
    Renderiza el menú lateral dinámico de la aplicación y gestiona la navegación.

    Utiliza el estado de sesión para persistir la página seleccionada y 
    construye la interfaz basándose en la estructura definida en 'MENU_STRUCTURE'.
    Incluye manejo de errores global para garantizar la estabilidad de la UI.

    Returns:
        str: El nombre de la página seleccionada actualmente por el usuario.

    Raises:
        Exception: Captura errores de renderizado para evitar bloqueos del sistema.
    """
    
    if KEY_PAGINA_ACTUAL not in st.session_state:
        st.session_state[KEY_PAGINA_ACTUAL] = LABEL_INICIO

    try:
        with st.sidebar:
            st.markdown("## 📊 Visor Aseguramiento")
            st.markdown("---")
            
            # 1. Lógica de Búsqueda
            todas_las_opciones = [LABEL_INICIO]
            for nombre, detalles in MENU_STRUCTURE.items():
                if detalles.get("type") == TIPO_GROUP:
                    todas_las_opciones.extend(list(detalles.get("items", {}).keys()))
                elif detalles.get("type") == TIPO_PAGE:
                    todas_las_opciones.append(nombre)
            
            busqueda = st.selectbox(
                "Búsqueda rápida", 
                options=[""] + todas_las_opciones, 
                format_func=lambda x: "Seleccione un reporte..." if x == "" else x
            )
            
            if busqueda:
                st.session_state[KEY_PAGINA_ACTUAL] = busqueda
                st.rerun()
                
            st.markdown("---")
            st.markdown("### Navegación Principal")
            
            # 2. Renderizar Inicio
            es_inicio = st.session_state[KEY_PAGINA_ACTUAL] == LABEL_INICIO
            if st.button(f"{MENU_STRUCTURE[LABEL_INICIO]['icon']} {LABEL_INICIO}", 
                         use_container_width=True, 
                         type="primary" if es_inicio else "secondary"):
                st.session_state[KEY_PAGINA_ACTUAL] = LABEL_INICIO
                st.rerun()
                
            # 3. Renderizado Dinámico de Grupos y Páginas
            for nombre, detalles in MENU_STRUCTURE.items():
                if nombre == LABEL_INICIO: continue
                
                # Caso Grupos
                if detalles.get("type") == TIPO_GROUP:
                    with st.expander(f"{detalles.get('icon', '')} {nombre}", expanded=True):
                        for nombre_item in detalles.get("items", {}).keys():
                            is_active = st.session_state[KEY_PAGINA_ACTUAL] == nombre_item
                            if st.button(nombre_item, use_container_width=True, key=nombre_item, 
                                         type="primary" if is_active else "secondary"):
                                st.session_state[KEY_PAGINA_ACTUAL] = nombre_item
                                st.rerun()
                
                # Caso Páginas Sueltas
                elif detalles.get("type") == TIPO_PAGE:
                    is_active = st.session_state[KEY_PAGINA_ACTUAL] == nombre
                    if st.button(f"{detalles.get('icon', '')} {nombre}", use_container_width=True, 
                                 key=nombre, type="primary" if is_active else "secondary"):
                        st.session_state[KEY_PAGINA_ACTUAL] = nombre
                        st.rerun()
            
            st.markdown("---")
            st.caption("© 2026 - Municipio de Envigado")
            
    except Exception as error:
        st.error("Error crítico en la carga del menú.")
        st.exception(error) # Muestra el error de forma técnica pero controlada
        
    return st.session_state[KEY_PAGINA_ACTUAL]