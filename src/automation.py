"""
Script principal de automatización.
"""

import logging
from src.api_client import APIClient
from src.data_processor import DataProcessor

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class APIAutomation:
    """Automatiza tareas repetitivas con APIs REST."""
    
    def __init__(self, api_url: str):
        """
        Inicializa la automatización.
        
        Args:
            api_url: URL base de la API a usar
        """
        self.api_client = APIClient(api_url)
        self.data_processor = DataProcessor()
    
    def fetch_and_process(self, endpoint: str, output_file: str = None) -> dict:
        """
        Obtiene datos de una API y los procesa.
        
        Args:
            endpoint: Endpoint a consultar
            output_file: Archivo de salida opcional
            
        Returns:
            Datos procesados
        """
        try:
            logger.info(f"Obteniendo datos de {endpoint}...")
            data = self.api_client.get(endpoint)
            
            if output_file:
                self.data_processor.save_to_json(data, output_file)
                logger.info(f"Datos guardados en {output_file}")
            
            return data
        except Exception as e:
            logger.error(f"Error durante la automatización: {str(e)}")
            raise
    
    def close(self):
        """Cierra conexiones."""
        self.api_client.close()


if __name__ == "__main__":
    # Ejemplo de uso
    API_URL = "https://jsonplaceholder.typicode.com"
    
    automation = APIAutomation(API_URL)
    
    # Obtener posts
    posts = automation.fetch_and_process("posts", "posts.json")
    logger.info(f"Se obtuvieron {len(posts)} posts")
    
    automation.close()

