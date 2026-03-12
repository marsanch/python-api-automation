"""
Cliente para conectar con APIs REST externas.
"""

import requests
import logging
from typing import Optional, Dict, Any

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class APIClient:
    """Cliente para realizar peticiones HTTP a APIs REST."""
    
    def __init__(self, base_url: str, timeout: int = 10):
        """
        Inicializa el cliente de API.
        
        Args:
            base_url: URL base de la API
            timeout: Tiempo máximo de espera en segundos
        """
        self.base_url = base_url
        self.timeout = timeout
        self.session = requests.Session()
    
    def get(self, endpoint: str, params: Optional[Dict] = None) -> Dict[str, Any]:
        """
        Realiza una petición GET a la API.
        
        Args:
            endpoint: Ruta del endpoint
            params: Parámetros de consulta
            
        Returns:
            Respuesta JSON de la API
        """
        try:
            url = f"{self.base_url}/{endpoint}"
            response = self.session.get(url, params=params, timeout=self.timeout)
            response.raise_for_status()
            logger.info(f"GET {url} - Status: {response.status_code}")
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"Error en GET request: {str(e)}")
            raise
    
    def post(self, endpoint: str, data: Optional[Dict] = None) -> Dict[str, Any]:
        """
        Realiza una petición POST a la API.
        
        Args:
            endpoint: Ruta del endpoint
            data: Datos a enviar en el cuerpo
            
        Returns:
            Respuesta JSON de la API
        """
        try:
            url = f"{self.base_url}/{endpoint}"
            response = self.session.post(url, json=data, timeout=self.timeout)
            response.raise_for_status()
            logger.info(f"POST {url} - Status: {response.status_code}")
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"Error en POST request: {str(e)}")
            raise
    
    def close(self):
        """Cierra la sesión."""
        self.session.close()
    
    def __enter__(self):
        """Context manager entry."""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.close()

