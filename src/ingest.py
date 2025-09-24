import pandas as pd
import os
from pathlib import Path
from typing import List, Dict, Any
import logging

class DataIngestor:
    def __init__(self, base_path: str = "data"):
        self.base_path = Path(base_path)
        self.raw_path = self.base_path / "raw"
        self.bronze_path = self.base_path / "bronze"
        self.setup_directories()
        
    def setup_directories(self):
        """Crear directorios necesarios"""
        self.raw_path.mkdir(parents=True, exist_ok=True)
        self.bronze_path.mkdir(parents=True, exist_ok=True)
        
    def discover_csv_files(self) -> List[Path]:
        """Descubrir archivos CSV en el directorio raw"""
        return list(self.raw_path.glob("*.csv"))
    
    def load_csv_with_detection(self, file_path: Path) -> pd.DataFrame:
        """Cargar CSV detectando automáticamente formato y encoding"""
        try:
            # Intentar diferentes encodings
            encodings = ['utf-8', 'latin-1', 'iso-8859-1', 'windows-1252']
            for encoding in encodings:
                try:
                    df = pd.read_csv(file_path, encoding=encoding)
                    logging.info(f"Archivo {file_path} cargado con encoding {encoding}")
                    return df
                except UnicodeDecodeError:
                    continue
            raise ValueError(f"No se pudo decodificar el archivo {file_path}")
        except Exception as e:
            logging.error(f"Error cargando {file_path}: {e}")
            raise
    
    def infer_schema(self, df: pd.DataFrame) -> Dict[str, str]:
        """Inferir schema del DataFrame"""
        schema = {}
        for col in df.columns:
            dtype = str(df[col].dtype)
            schema[col] = dtype
        return schema
    
    def save_to_bronze(self, df: pd.DataFrame, filename: str):
        """Guardar datos en capa bronze en formato Parquet"""
        output_path = self.bronze_path / f"{Path(filename).stem}.parquet"
        df.to_parquet(output_path, index=False)
        logging.info(f"Datos guardados en bronze: {output_path}")

def main():
    """Función principal para testing"""
    ingestor = DataIngestor()
    files = ingestor.discover_csv_files()
    print(f"Archivos encontrados: {files}")

if __name__ == "__main__":
    main()
