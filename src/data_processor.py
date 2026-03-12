"""
Procesador de datos obtenidos de APIs.
"""

import json
import logging
from typing import List, Dict, Any
from datetime import datetime

logger = logging.getLogger(__name__)


class DataProcessor:
    """Procesa y transforma datos obtenidos de APIs."""
    
    @staticmethod
    def filter_data(data: List[Dict], key: str, value: Any) -> List[Dict]:
        """
        Filtra datos basado en una clave y valor.
        
        Args:
            data: Lista de diccionarios
            key: Clave para filtrar
            value: Valor a buscar
            
        Returns:
            Lista filtrada
        """
        filtered = [item for item in data if item.get(key) == value]
        logger.info(f"Datos filtrados: {len(filtered)} elementos")
        return filtered
    
    @staticmethod
    def extract_fields(data: List[Dict], fields: List[str]) -> List[Dict]:
        """
        Extrae campos específicos de los datos.
        
        Args:
            data: Lista de diccionarios
            fields: Campos a extraer
            
        Returns:
            Lista con solo los campos especificados
        """
        extracted = [{field: item.get(field) for field in fields} for item in data]
        logger.info(f"Campos extraídos: {fields}")
        return extracted
    
    @staticmethod
    def save_to_json(data: Any, filename: str) -> None:
        """
        Guarda datos en un archivo JSON.
        
        Args:
            data: Datos a guardar
            filename: Nombre del archivo
        """
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            logger.info(f"Datos guardados en {filename}")
        except IOError as e:
            logger.error(f"Error al guardar archivo: {str(e)}")
            raise
    
    @staticmethod
    def load_from_json(filename: str) -> Any:
        """
        Carga datos desde un archivo JSON.
        
        Args:
            filename: Nombre del archivo
            
        Returns:
            Datos cargados
        """
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
            logger.info(f"Datos cargados desde {filename}")
            return data
        except IOError as e:
            logger.error(f"Error al cargar archivo: {str(e)}")
            raise

