import streamlit as st
import pandas as pd
from src.ingest import DataIngestor
from src.validate import DataValidator
from src.transform import DataTransformer

def main():
    st.title("📊 Pipeline de Datos: CSV a Almacén Analítico")
    st.write("Laboratorio de procesamiento de datos heterogéneos")
    
    # Sidebar para navegación
    page = st.sidebar.selectbox(
        "Selecciona una página:",
        ["Inicio", "Ingesta", "Validación", "Transformación", "Dashboard"]
    )
    
    if page == "Inicio":
        show_home()
    elif page == "Ingesta":
        show_ingestion()
    elif page == "Validación":
        show_validation()
    elif page == "Transformación":
        show_transformation()
    elif page == "Dashboard":
        show_dashboard()

def show_home():
    st.header("🏠 Página de Inicio")
    st.write("""
    Esta aplicación demuestra el pipeline completo de procesamiento de datos:
    - **Ingesta**: Carga de múltiples archivos CSV
    - **Validación**: Control de calidad y consistencia
    - **Transformación**: Normalización y enriquecimiento
    - **Almacenamiento**: Capas Bronze, Silver, Gold
    """)

def show_ingestion():
    st.header("📥 Módulo de Ingesta")
    # Implementar interfaz de ingesta aquí

def show_validation():
    st.header("✅ Módulo de Validación")
    # Implementar interfaz de validación aquí

def show_transformation():
    st.header("🔄 Módulo de Transformación")
    # Implementar interfaz de transformación aquí

def show_dashboard():
    st.header("📈 Dashboard de Métricas")
    # Implementar dashboard aquí

if __name__ == "__main__":
    main()
