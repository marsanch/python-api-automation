"""
Tests para el cliente de API.
"""

import pytest
import requests
from unittest.mock import patch, MagicMock
from src.api_client import APIClient


class TestAPIClient:
    """Tests del APIClient."""
    
    @pytest.fixture
    def client(self):
        """Fixture que crea un cliente de API."""
        return APIClient("https://api.example.com")
    
    @patch('src.api_client.requests.Session.get')
    def test_get_success(self, mock_get, client):
        """Test para GET request exitoso."""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"id": 1, "name": "Test"}
        mock_get.return_value = mock_response
        
        result = client.get("test")
        
        assert result == {"id": 1, "name": "Test"}
        mock_get.assert_called_once()
    
    @patch('src.api_client.requests.Session.get')
    def test_get_error(self, mock_get, client):
        """Test para GET request con error."""
        mock_get.side_effect = requests.exceptions.RequestException("Error")
        
        with pytest.raises(requests.exceptions.RequestException):
            client.get("test")
    
    @patch('src.api_client.requests.Session.post')
    def test_post_success(self, mock_post, client):
        """Test para POST request exitoso."""
        mock_response = MagicMock()
        mock_response.status_code = 201
        mock_response.json.return_value = {"id": 1, "name": "Test"}
        mock_post.return_value = mock_response
        
        result = client.post("test", {"name": "Test"})
        
        assert result == {"id": 1, "name": "Test"}
        mock_post.assert_called_once()
    
    def test_context_manager(self):
        """Test que el cliente funciona como context manager."""
        with APIClient("https://api.example.com") as client:
            assert client is not None

