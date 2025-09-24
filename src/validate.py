import pandas as pd
import numpy as np
from typing import Dict, List, Tuple
import logging
from pathlib import Path

class DataValidator:
    def __init__(self):
        self.validation_results = {}
        
    def validate_schema(self, df: pd.DataFrame, expected_schema: Dict) -> Dict:
        """Validar que el schema coincide con el esperado"""
        results = {
            'passed': True,
            'errors': [],
            'warnings': []
        }
        
        # Verificar columnas esperadas
        expected_cols = set(expected_schema.keys())
        actual_cols = set(df.columns)
        
        missing_cols = expected_cols - actual_cols
        extra_cols = actual_cols - expected_cols
        
        if missing_cols:
            results['passed'] = False
            results['errors'].append(f"Columnas faltantes: {missing_cols}")
            
        if extra_cols:
            results['warnings'].append(f"Columnas extra: {extra_cols}")
        
        # Verificar tipos de datos
        for col, expected_type in expected_schema.items():
            if col in df.columns:
                actual_type = str(df[col].dtype)
                if expected_type != actual_type:
                    results['warnings'].append(
                        f"Tipo discrepante en {col}: esperado {expected_type}, actual {actual_type}"
                    )
        
        return results
    
    def check_completeness(self, df: pd.DataFrame) -> Dict:
        """Verificar completitud de los datos"""
        total_rows = len(df)
        completeness = {}
        
        for col in df.columns:
            non_null_count = df[col].count()
            null_count = df[col].isnull().sum()
            completeness[col] = {
                'non_null_count': non_null_count,
                'null_count': null_count,
                'completeness_rate': non_null_count / total_rows * 100
            }
        
        return completeness
    
    def check_uniqueness(self, df: pd.DataFrame, unique_columns: List[str]) -> Dict:
        """Verificar unicidad en columnas específicas"""
        uniqueness = {}
        
        for col in unique_columns:
            if col in df.columns:
                total_count = len(df[col])
                unique_count = df[col].nunique()
                uniqueness[col] = {
                    'total_count': total_count,
                    'unique_count': unique_count,
                    'duplicate_count': total_count - unique_count,
                    'uniqueness_rate': unique_count / total_count * 100
                }
        
        return uniqueness
    
    def generate_quality_report(self, df: pd.DataFrame, schema: Dict) -> Dict:
        """Generar reporte completo de calidad"""
        report = {
            'schema_validation': self.validate_schema(df, schema),
            'completeness': self.check_completeness(df),
            'basic_stats': self.get_basic_statistics(df)
        }
        
        return report
    
    def get_basic_statistics(self, df: pd.DataFrame) -> Dict:
        """Obtener estadísticas básicas del DataFrame"""
        return df.describe(include='all').to_dict()

def main():
    """Función principal para testing"""
    validator = DataValidator()
    print("Módulo de validación cargado correctamente")

if __name__ == "__main__":
    main()
