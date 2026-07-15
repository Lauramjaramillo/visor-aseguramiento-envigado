import streamlit as st
from src.config import MENU_STRUCTURE

def render_sidebar():
    if "pagina_actual" not in st.session_state:
        st.session_state.pagina_actual = "Inicio"

    with st.sidebar:
        st.markdown("## 📊 Visor Aseguramiento")
        st.markdown("---")
        
        # 1. Búsqueda rápida (Actualizada para incluir páginas)
        todas_las_opciones = ["Inicio"]
        for key, val in MENU_STRUCTURE.items():
            if val["type"] == "group":
                todas_las_opciones.extend(list(val["items"].keys()))
            elif val["type"] == "page":
                todas_las_opciones.append(key)
        
        busqueda = st.selectbox(
            "Búsqueda rápida", 
            options=[""] + todas_las_opciones, 
            format_func=lambda x: "Seleccione un reporte..." if x == "" else x
        )
        
        if busqueda != "":
            st.session_state.pagina_actual = busqueda
            st.rerun()
            
        st.markdown("---")
        st.markdown("### Navegación Principal")
        
        # 2. Renderizar Inicio
        if st.button(f"{MENU_STRUCTURE['Inicio']['icon']} Inicio", use_container_width=True, type="primary" if st.session_state.pagina_actual == "Inicio" else "secondary"):
            st.session_state.pagina_actual = "Inicio"
            st.rerun()
            
        # 3. Renderizar Grupos y Páginas (AQUÍ ESTABA LA OMISIÓN)
        for nombre, detalles in MENU_STRUCTURE.items():
            if nombre == "Inicio": continue
            
            # Caso A: Si es un grupo
            if detalles["type"] == "group":
                with st.expander(f"{detalles['icon']} {nombre}", expanded=True):
                    for nombre_item in detalles["items"].keys():
                        tipo_btn = "primary" if st.session_state.pagina_actual == nombre_item else "secondary"
                        if st.button(nombre_item, use_container_width=True, key=nombre_item, type=tipo_btn):
                            st.session_state.pagina_actual = nombre_item
                            st.rerun()
            
            # Caso B: Si es una página suelta (Directorio)
            elif detalles["type"] == "page":
                tipo_btn = "primary" if st.session_state.pagina_actual == nombre else "secondary"
                if st.button(f"{detalles['icon']} {nombre}", use_container_width=True, key=nombre, type=tipo_btn):
                    st.session_state.pagina_actual = nombre
                    st.rerun()
        
        st.markdown("---")
        st.caption("© 2026 - Municipio de Envigado")
        
    return st.session_state.pagina_actual