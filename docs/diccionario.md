# Diccionario de Datos

## Estructura del Proyecto

### Capas de Datos

| Capa | Descripción | Formato | Ubicación |
|------|-------------|---------|-----------|
| Raw | Datos originales sin procesar | CSV | `data/raw/` |
| Bronze | Datos crudos preservados | Parquet | `data/bronze/` |
| Silver | Datos limpios y normalizados | Parquet | `data/silver/` |
| Gold | Datos enriquecidos para análisis | Parquet | `data/gold/` |

## Schemas Esperados

### Ejemplo de Schema para Datos de Ventas
```python
sales_schema = {
    'order_id': 'string',
    'order_date': 'datetime64[ns]',
    'customer_id': 'string',
    'product_id': 'string',
    'quantity': 'int64',
    'unit_price': 'float64',
    'total_amount': 'float64',
    'region': 'string'
}
