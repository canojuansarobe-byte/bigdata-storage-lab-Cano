import pandas as pd
import numpy as np
from typing import Dict, List
import logging
from pathlib import Path

class DataTransformer:
    def __init__(self):
        self.transformations_applied = []
        
    def standardize_column_names(self, df: pd.DataFrame) -> pd.DataFrame:
        """Estandarizar nombres de columnas a snake_case"""
        df_clean = df.copy()
        df_clean.columns = [
            col.strip().lower().replace(' ', '_').replace('-', '_')
            for col in df_clean.columns
        ]
        self.transformations_applied.append("standardize_column_names")
        return df_clean
    
    def handle_missing_values(self, df: pd.DataFrame, strategy: Dict) -> pd.DataFrame:
        """Manejar valores faltantes según estrategia especificada"""
        df_clean = df.copy()
        
        for col, method in strategy.items():
            if col in df_clean.columns:
                if method == 'drop':
                    df_clean = df_clean.dropna(subset=[col])
                elif method == 'mean':
                    df_clean[col] = df_clean[col].fillna(df_clean[col].mean())
                elif method == 'median':
                    df_clean[col] = df_clean[col].fillna(df_clean[col].median())
                elif method == 'mode':
                    df_clean[col] = df_clean[col].fillna(df_clean[col].mode()[0])
                elif method == 'ffill':
                    df_clean[col] = df_clean[col].fillna(method='ffill')
        
        self.transformations_applied.append("handle_missing_values")
        return df_clean
    
    def normalize_data_types(self, df: pd.DataFrame, type_mapping: Dict) -> pd.DataFrame:
        """Normalizar tipos de datos según mapping especificado"""
        df_clean = df.copy()
        
        for col, target_type in type_mapping.items():
            if col in df_clean.columns:
                try:
                    if target_type == 'datetime':
                        df_clean[col] = pd.to_datetime(df_clean[col])
                    elif target_type == 'numeric':
                        df_clean[col] = pd.to_numeric(df_clean[col], errors='coerce')
                    elif target_type == 'category':
                        df_clean[col] = df_clean[col].astype('category')
                    elif target_type == 'string':
                        df_clean[col] = df_clean[col].astype(str)
                except Exception as e:
                    logging.warning(f"Error convirtiendo {col} a {target_type}: {e}")
        
        self.transformations_applied.append("normalize_data_types")
        return df_clean
    
    def remove_duplicates(self, df: pd.DataFrame, subset: List[str] = None) -> pd.DataFrame:
        """Eliminar duplicados basado en columnas específicas"""
        df_clean = df.drop_duplicates(subset=subset)
        duplicates_removed = len(df) - len(df_clean)
        
        if duplicates_removed > 0:
            logging.info(f"Removidos {duplicates_removed} registros duplicados")
        
        self.transformations_applied.append("remove_duplicates")
        return df_clean
    
    def apply_transformation_pipeline(self, df: pd.DataFrame, 
                                    cleaning_rules: Dict) -> pd.DataFrame:
        """Aplicar pipeline completo de transformaciones"""
        df_transformed = df.copy()
        
        # Aplicar transformaciones en orden
        if cleaning_rules.get('standardize_columns', False):
            df_transformed = self.standardize_column_names(df_transformed)
            
        if 'missing_values_strategy' in cleaning_rules:
            df_transformed = self.handle_missing_values(
                df_transformed, cleaning_rules['missing_values_strategy']
            )
            
        if 'type_mapping' in cleaning_rules:
            df_transformed = self.normalize_data_types(
                df_transformed, cleaning_rules['type_mapping']
            )
            
        if cleaning_rules.get('remove_duplicates', False):
            subset = cleaning_rules.get('duplicate_subset', None)
            df_transformed = self.remove_duplicates(df_transformed, subset)
        
        return df_transformed

def main():
    """Función principal para testing"""
    transformer = DataTransformer()
    print("Módulo de transformación cargado correctamente")

if __name__ == "__main__":
    main()
