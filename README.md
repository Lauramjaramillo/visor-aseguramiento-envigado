```markdown
# Portal de Gestión del Aseguramiento - Envigado

Portal centralizado para la consulta de estadísticas de aseguramiento, reportes de presupuesto y acceso rápido a plataformas oficiales de seguridad social para la administración municipal.

## 📋 Descripción
Esta aplicación ha sido desarrollada bajo una arquitectura modular para garantizar su escalabilidad y mantenibilidad. El sistema centraliza el acceso a informes interactivos (Power BI), reportes de gestión y un directorio de consultas externas, proporcionando un entorno seguro y eficiente para el apoyo a la toma de decisiones y el ejercicio de las funciones del área de aseguramiento.

## 🚀 Arquitectura Técnica
El proyecto implementa estándares de desarrollo profesional:
* **Patrón Despachador:** Lógica de enrutamiento centralizada para un escalado limpio y eficiente.
* **Modularidad:** Separación estricta de configuraciones (`config.py`) y lógica de interfaz (`views/`, `components/`).
* **Robustez:** Manejo de errores global (`try-except`) y validación de tipos (`typing`) para una mayor estabilidad.
* **Identidad Institucional:** Integración de elementos visuales (escudo institucional) para oficializar el entorno de trabajo.

## 🛠 Instalación

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/Lauramjaramillo/visor-aseguramiento-envigado.git](https://github.com/Lauramjaramillo/visor-aseguramiento-envigado.git)
   cd visor-aseguramiento-envigado

```

2. **Crear entorno virtual:**
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

```


3. **Instalar dependencias:**
```bash
pip install streamlit

```


4. **Ejecutar la aplicación:**
```bash
streamlit run app.py

```



## 📁 Estructura del Proyecto

```text
├── assets/             # Recursos visuales (escudo institucional)
├── src/
│   ├── components/     # Componentes de UI reutilizables
│   ├── views/          # Lógica de renderizado de vistas
│   └── config.py       # Configuración centralizada de menús y enlaces
├── app.py              # Punto de entrada y controlador principal (Dispatcher)
└── .gitignore          # Exclusión de archivos temporales

```

## 👤 Autor

Laura María Jaramillo Sanchez

```