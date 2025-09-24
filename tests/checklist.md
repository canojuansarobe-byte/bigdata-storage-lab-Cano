# Checklist de Calidad

## ✅ Pre-requisitos
- [ ] Python 3.8+ instalado
- [ ] Dependencias instaladas (`requirements.txt`)
- [ ] Estructura de directorios creada
- [ ] Archivos de datos de prueba disponibles

## 🔄 Pipeline de Datos

### Ingesta
- [ ] Los archivos CSV se cargan correctamente
- [ ] Se detectan automáticamente encoding y delimitadores
- [ ] Los metadatos de ingesta se registran apropiadamente
- [ ] Los datos se guardan en formato Parquet en bronze

### Validación
- [ ] El schema de datos es validado contra el esperado
- [ ] Se calculan métricas de completitud
- [ ] Se verifican constraints de negocio
- [ ] Se generan reportes de calidad

### Transformación
- [ ] Los nombres de columnas se estandarizan
- [ ] Los valores faltantes se manejan apropiadamente
- [ ] Los tipos de datos se normalizan
- [ ] Los duplicados se eliminan

## 📊 Capas de Datos

### Bronze Layer
- [ ] Datos crudos preservados sin alteración
- [ ] Formato columnar eficiente (Parquet)
- [ ] Metadatos de procedencia incluidos

### Silver Layer
- [ ] Datos limpios y normalizados
- [ ] Schema consistente aplicado
- [ ] Calidad de datos verificada

### Gold Layer
- [ ] Datos enriquecidos con business logic
- [ ] Modelo dimensional implementado
- [ ] Optimizado para consultas analíticas

## 🚀 Entrega Final

### Repositorio
- [ ] Estructura de archivos correcta
- [ ] README.md completo y claro
- [ ] Documentación técnica actualizada
- [ ] Código bien comentado y organizado

### Aplicación Streamlit
- [ ] Dashboard funcional
- [ ] Visualización de métricas
- [ ] Interfaz intuitiva
- [ ] Procesos ejecutables desde la UI
