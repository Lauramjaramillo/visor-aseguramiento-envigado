import streamlit as st
from typing import Dict, Any
from src.config import MENU_STRUCTURE

# Constantes para evitar errores de tipo "Magic Strings"
KEY_PAGINA_ACTUAL = "pagina_actual"
TIPO_GROUP = "group"
TIPO_PAGE = "page"
LABEL_INICIO = "Inicio"

def actualizar_pagina():
    """
    Callback que se ejecuta al seleccionar una opción en el buscador.
    Actualiza la página actual y limpia el buscador.
    """
    seleccion = st.session_state["buscador_sidebar"]
    if seleccion:
        st.session_state[KEY_PAGINA_ACTUAL] = seleccion
    # Limpiamos el buscador para que vuelva a decir "Seleccione un reporte..."
    st.session_state["buscador_sidebar"] = ""

def render_sidebar() -> str:
    """
    Renderiza el menú lateral dinámico de la aplicación y gestiona la navegación.
    """
    
    if KEY_PAGINA_ACTUAL not in st.session_state:
        st.session_state[KEY_PAGINA_ACTUAL] = LABEL_INICIO

    try:
        with st.sidebar:
            st.markdown("## 📊 Gestión del Aseguramiento")
            st.markdown("---")
            
            # 1. Lógica de Búsqueda
            todas_las_opciones = [LABEL_INICIO]
            for nombre, detalles in MENU_STRUCTURE.items():
                if detalles.get("type") == TIPO_GROUP:
                    todas_las_opciones.extend(list(detalles.get("items", {}).keys()))
                elif detalles.get("type") == TIPO_PAGE:
                    todas_las_opciones.append(nombre)
            
            # El selectbox dispara 'actualizar_pagina' al cambiar
            st.selectbox(
                "Búsqueda rápida", 
                options=[""] + todas_las_opciones, 
                format_func=lambda x: "Seleccione un reporte..." if x == "" else x,
                key="buscador_sidebar",
                on_change=actualizar_pagina
            )
            
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
            
            # PASO A: Primero renderizamos todos los Grupos
            for nombre, detalles in MENU_STRUCTURE.items():
                if nombre == LABEL_INICIO or detalles.get("type") != TIPO_GROUP: 
                    continue
                
                with st.expander(f"{detalles.get('icon', '')} {nombre}", expanded=True):
                    for nombre_item in detalles.get("items", {}).keys():
                        is_active = st.session_state[KEY_PAGINA_ACTUAL] == nombre_item
                        if st.button(nombre_item, use_container_width=True, key=nombre_item, 
                                    type="primary" if is_active else "secondary"):
                            st.session_state[KEY_PAGINA_ACTUAL] = nombre_item
                            st.rerun()

            # PASO B: Luego renderizamos todas las Páginas Sueltas (incluyendo el Directorio)
            for nombre, detalles in MENU_STRUCTURE.items():
                if nombre == LABEL_INICIO or detalles.get("type") != TIPO_PAGE: 
                    continue
                
                is_active = st.session_state[KEY_PAGINA_ACTUAL] == nombre
                if st.button(f"{detalles.get('icon', '🌐')} {nombre}", use_container_width=True, 
                            key=nombre, type="primary" if is_active else "secondary"):
                    st.session_state[KEY_PAGINA_ACTUAL] = nombre
                    st.rerun()
            
            st.markdown("---")
            st.caption("© 2026 - Municipio de Envigado - Dirección de Aseguramiento")
            
    except Exception as error:
        st.error("Error crítico en la carga del menú.")
        st.exception(error)
        
    return st.session_state[KEY_PAGINA_ACTUAL]