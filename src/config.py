# src/config.py

MENU_STRUCTURE = {
    "Inicio": {"type": "home", "icon": "🏠"},
    "Estadísticas Aseguramiento": {
        "type": "group",
        "icon": "📊",
        "items": {
            "Estadísticas 2026": "https://app.powerbi.com/view?r=eyJrIjoiYzM0ZjJjOGQtNjE2Zi00ZDQ3LTg3NzItNzliYWFkMThhYzMxIiwidCI6IjA3MzljZmI3LWJhNTEtNDc3ZS05NWYxLWYxYmRkMWYzMTEzMCIsImMiOjR9",
            "Estadísticas 2025": "https://app.powerbi.com/view?r=eyJrIjoiYmQ4MGUyOTItZWE5Mi00NTYyLTliNDYtYjcwNmE3YTFkOGFkIiwidCI6IjA3MzljZmI3LWJhNTEtNDc3ZS05NWYxLWYxYmRkMWYzMTEzMCIsImMiOjR9",
            "Estadísticas 2024": "https://app.powerbi.com/view?r=eyJrIjoiMzM1MGE0Y2EtNmY0MC00OGFlLWIwZWYtMDRmNjg3ODJmOWEwIiwidCI6IjA3MzljZmI3LWJhNTEtNDc3ZS05NWYxLWYxYmRkMWYzMTEzMCIsImMiOjR9",
        }
    },
    "Reportes Nacionales": {
        "type": "group",
        "icon": "🏛️",
        "items": {
            "Aseguramiento DSSA": "https://app.powerbi.com/view?r=eyJrIjoiZjE4ZjY5MjAtYTIxYi00N2UzLWJhMjEtYzE1NjZkMzcwNjhjIiwidCI6IjY0MmYxNTllLThmMTItNDMwOS1iODdjLWNiYzU0MzZlYzY5MSIsImMiOjR9",
            "Cifras Ministerio de Salud": "https://app.powerbi.com/view?r=eyJrIjoiY2JmZGUyNzgtMGQ3My00MDIwLTkyZTYtMTI5ODA0M2UwMmQ0IiwidCI6ImJmYjdlMTNhLTdmYjctNDAxNi04MzBjLWQzNzE2ZThkZDhiOCJ9&pageName=df59cad96749df5e3ddd",
        }
    },
    "ROCA": {
        "type": "group",
        "icon": "💰",
        "items": {
            "ROCA 2026": "https://app.powerbi.com/view?r=eyJrIjoiZThhMGY1YzUtODVlNy00M2NmLWFlNmQtYjJiYjhjNTFkNzIzIiwidCI6IjA3MzljZmI3LWJhNTEtNDc3ZS05NWYxLWYxYmRkMWYzMTEzMCIsImMiOjR9",
            "ROCA 2025": "https://app.powerbi.com/view?r=eyJrIjoiMTVmNmM4NzEtYzQzNS00ZjI2LWE4OGQtMTk5OTZiYjJjMDc1IiwidCI6IjA3MzljZmI3LWJhNTEtNDc3ZS05NWYxLWYxYmRkMWYzMTEzMCIsImMiOjR9",
            
        }
    },
    "Directorio de Consultas": {"type": "page", "icon": "🌐"}
}

ENLACES_EXTERNOS = {
    "Plataformas de Afiliación y Seguridad Social": [
        {"nombre": "Consulta EPS (ADRES)", "url": "https://www.adres.gov.co/consulte-su-eps", "desc": "Verificación del estado de aseguramiento en salud."},
        {"nombre": "Consulta Sisbén IV", "url": "https://reportes.sisben.gov.co/dnp_sisbenconsulta", "desc": "Identificación de grupo poblacional y estado del Sisbén IV."},
        {"nombre": "BDUA - Regímenes de Excepción", "url": "https://aplicaciones.adres.gov.co/BDUA_Internet/Pages/ConsultarAfiliadoWebBDEX.aspx?pag=4099", "desc": "Validación de afiliados en regímenes especiales y exceptuados."},
        {"nombre": "Mi Seguridad Social", "url": "https://miseguridadsocial.gov.co/", "desc": "Gestión centralizada de afiliaciones y reporte de novedades."},
        {"nombre": "Savia Salud - Certificados", "url": "https://www.saviasaludeps.com/sitioweb/tramites-en-linea/certificado-de-afiliacion", "desc": "Certificados de afiliación a SAVIA SALUD EPS."}
    ],
    "Auditoría y Gestión de Novedades": [
        {"nombre": "SISBÉN - Portal de Solicitudes", "url": "https://reportes.sisben.gov.co/DNP_PortalUnicoSolicitudes/Modulo/Frontend/Login.aspx", "desc": "Consultas masivas a la base de datos de SISBÉN IV."},
        {"nombre": "VIVANTO - Víctimas", "url": "https://vivantov2.unidadvictimas.gov.co/", "desc": "Consulta de estatus en el Registro Único de Víctimas (RUV)."},
        {"nombre": "Procuraduría - Antecedentes", "url": "https://www.procuraduria.gov.co/Pages/Consulta-de-Antecedentes.aspx", "desc": "Certificación de antecedentes disciplinarios vigentes."},
        {"nombre": "Defunciones Registraduría", "url": "https://defunciones.registraduria.gov.co/", "desc": "Verificación de novedades por fallecimiento mediante documento."},
        {"nombre": "Certificados Registraduría (BDUA)", "url": "https://consultasrc.registraduria.gov.co:28080/ProyectoSCCRC/", "desc": "Consulta de registros civiles y bases de datos de nacimiento."},
        {"nombre": "INPEC - Población Privada de la Libertad", "url": "https://www.inpec.gov.co/registro-de-la-poblacion-privada-de-la-libertad", "desc": "Consulta de registros oficiales de personas privadas de la libertad."}
    ],
    "Financiamiento y Compensación ADRES": [
        {"nombre": "Liquidaciones y Restituciones", "url": "https://www.adres.gov.co/eps/regimen-subsidiado/liquidaciones-y-restituciones-por-afiliado", "desc": "Consulta de saldos financieros por afiliado (Régimen Subsidiado)."},
        {"nombre": "Afiliados Compensados", "url": "https://www.adres.gov.co/eps/regimen-contributivo/Paginas/afiliados-compensados.aspx", "desc": "Auditoría de procesos de compensación del Régimen Contributivo."}
    ]
}

TEXTO_BIENVENIDA = """
### Portal de Gestión del Aseguramiento - Envigado
Bienvenido al sistema centralizado de consulta y seguimiento. Este portal facilita 
el acceso a indicadores estratégicos, reportes financieros y plataformas oficiales 
de validación, consolidando la información necesaria para el ejercicio de las 
funciones en el marco del aseguramiento en salud del municipio.
"""