"""
Tests para el procesador de datos.
"""

import pytest
import json
import tempfile
from src.data_processor import DataProcessor


class TestDataProcessor:
    """Tests del DataProcessor."""
    
    @pytest.fixture
    def sample_data(self):
        """Fixture con datos de ejemplo."""
        return [
            {"id": 1, "name": "Alice", "active": True},
            {"id": 2, "name": "Bob", "active": False},
            {"id": 3, "name": "Charlie", "active": True},
        ]
    
    def test_filter_data(self, sample_data):
        """Test para filtrar datos."""
        result = DataProcessor.filter_data(sample_data, "active", True)
        
        assert len(result) == 2
        assert all(item["active"] is True for item in result)
    
    def test_extract_fields(self, sample_data):
        """Test para extraer campos específicos."""
        result = DataProcessor.extract_fields(sample_data, ["id", "name"])
        
        assert len(result) == 3
        assert "active" not in result[0]
        assert "id" in result[0]
        assert "name" in result[0]
    
    def test_save_and_load_json(self, sample_data):
        """Test para guardar y cargar JSON."""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            filename = f.name
        
        try:
            DataProcessor.save_to_json(sample_data, filename)
            loaded_data = DataProcessor.load_from_json(filename)
            
            assert loaded_data == sample_data
        finally:
            import os
            os.unlink(filename)
    
    def test_save_json_error(self):
        """Test para error al guardar JSON."""
        with pytest.raises(IOError):
            DataProcessor.save_to_json({}, "/root/invalid/path/file.json")
    
    def test_load_json_error(self):
        """Test para error al cargar JSON."""
        with pytest.raises(IOError):
            DataProcessor.load_from_json("/nonexistent/file.json")

