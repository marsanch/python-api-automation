# Python API Automation

Automatización de procesos usando APIs con Python.

## Tecnologías

- **Python 3.12.7** - Lenguaje de programación
- **Requests** - Biblioteca para peticiones HTTP
- **Pytest** - Framework de testing
- **APIs REST** - Integración con servicios externos
- **JSON** - Procesamiento de datos

## Funcionalidades

- ✅ Conexión con APIs externas REST
- ✅ Procesamiento y transformación de datos
- ✅ Automatización de tareas repetitivas
- ✅ Manejo de errores y reintentos
- ✅ Logging integrado
- ✅ Suite completa de tests unitarios

## Estructura del Proyecto

```
python-api-automation/
├── src/                          # Código fuente
│   ├── __init__.py
│   ├── api_client.py            # Cliente HTTP para APIs
│   ├── data_processor.py         # Procesador de datos
│   └── automation.py             # Script principal de automatización
├── tests/                        # Tests unitarios
│   ├── __init__.py
│   ├── test_api_client.py
│   └── test_data_processor.py
├── config/                       # Archivos de configuración
│   └── .example_env
├── requirements.txt              # Dependencias Python
├── pytest.ini                    # Configuración de pytest
└── README.md                     # Este archivo
```

## Instalación

### Requisitos Previos

- Python 3.12.7 (configurado con pyenv)
- pip

### Pasos de Instalación

1. **Activar el entorno virtual (automático con .python-version)**:
   ```bash
   cd python-api-automation
   ```

2. **Instalar dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configurar variables de entorno** (opcional):
   ```bash
   cp config/.example_env .env
   ```

## Uso

### Ejecutar la Automatización

```bash
python -m src.automation
```

Este comando:
- Conecta con la API JSONPlaceholder
- Obtiene los datos (ejemplo: posts)
- Procesa los datos
- Guarda el resultado en `posts.json`

### Ejecutar Tests

```bash
pytest tests/ -v
```

### Ejemplo de Uso en Python

```python
from src.api_client import APIClient
from src.data_processor import DataProcessor

# Crear cliente de API
client = APIClient("https://jsonplaceholder.typicode.com")

# Obtener datos
posts = client.get("posts")

# Procesar datos
processor = DataProcessor()
processor.save_to_json(posts, "output.json")

# Cerrar conexión
client.close()
```

## Módulos Principales

### APIClient

Cliente para realizar peticiones HTTP a APIs REST:

- `get(endpoint, params)` - Realizar peticiones GET
- `post(endpoint, data)` - Realizar peticiones POST
- Manejo automático de errores
- Logging integrado

### DataProcessor

Procesador de datos JSON:

- `filter_data()` - Filtrar datos por clave-valor
- `extract_fields()` - Extraer campos específicos
- `save_to_json()` - Guardar datos en JSON
- `load_from_json()` - Cargar datos desde JSON

## Testing

El proyecto incluye 9 tests unitarios que cubren:

- ✅ Peticiones GET/POST exitosas
- ✅ Manejo de errores de conexión
- ✅ Context managers
- ✅ Filtrado de datos
- ✅ Extracción de campos
- ✅ Guardado/carga de JSON

Ejecutar tests:
```bash
pytest tests/ -v --cov
```

## Configuración

Variables de configuración en `config/.example_env`:

```
API_BASE_URL=https://jsonplaceholder.typicode.com
API_TIMEOUT=10
OUTPUT_DIR=./output
LOG_LEVEL=INFO
```

## Logging

El proyecto usa el módulo `logging` integrado de Python:

- Nivel por defecto: INFO
- Formato: Timestamp, Nombre del módulo, Nivel, Mensaje

## Ejemplo de Ejecución

```bash
(python-api-automation) $ python -m src.automation
INFO:__main__:Obteniendo datos de posts...
INFO:src.api_client:GET https://jsonplaceholder.typicode.com/posts - Status: 200
INFO:src.data_processor:Datos guardados en posts.json
INFO:__main__:Datos guardados en posts.json
INFO:__main__:Se obtuvieron 100 posts
```

## Contribución

1. Crear una rama para tu feature: `git checkout -b feature/AmazingFeature`
2. Commit tus cambios: `git commit -m 'Add some AmazingFeature'`
3. Push a la rama: `git push origin feature/AmazingFeature`
4. Abrir un Pull Request

## Próximas Mejoras

- [ ] Agregar autenticación (API keys, OAuth)
- [ ] Implementar retry logic con exponential backoff
- [ ] Agregar caching de datos
- [ ] Crear interfaz CLI con Click
- [ ] Agregar base de datos (SQLAlchemy)
- [ ] Dockerizar la aplicación


