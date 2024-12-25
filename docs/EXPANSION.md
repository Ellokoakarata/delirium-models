# 🧪 Guía de Expansión EsquizoAI 🧪

## 🔮 Agregar Nuevos Modelos

### 1. Estructura Base
Para agregar un nuevo modelo, sigue este patrón en `/scripts`:
```python
class NuevoModeloClient:
    def __init__(self, model_name, temperature, top_p, max_output_tokens):
        self.model_name = model_name
        self.temperature = temperature
        self.top_p = top_p
        self.max_output_tokens = max_output_tokens
        # Inicializar cliente específico del modelo
        
    def send_message(self, message):
        # Implementar lógica de envío
        # Debe retornar string con la respuesta
        pass
```



### 2. Configuración
En `/config/models_config.json`, agrega:
```json
{
    "nuevo_modelo": {
        "model_name": "nombre-del-modelo",
        "temperature": 0.9,
        "top_p": 0.95,
        "max_output_tokens": 1000,
        "prompt_file": "nuevo_modelo_prompt.txt"
    }
}
```

### 3. Prompts Base
En `/prompts`, crea:
- `nuevo_modelo_prompt.txt` con el prompt inicial

## 🎭 Multi-Modalidades

### 1. Imágenes
Para agregar procesamiento de imágenes:
```python
class ImageProcessor:
    def process_image(self, image_path):
        # Procesar imagen
        pass
    
    def generate_image(self, prompt):
        # Generar imagen
        pass
```

### 2. Audio
Para procesamiento de audio:
```python
class AudioProcessor:
    def text_to_speech(self, text):
        # Convertir texto a audio
        pass
    
    def speech_to_text(self, audio_path):
        # Convertir audio a texto
        pass
```

### 3. Video
Para generación/procesamiento de video:
```python
class VideoProcessor:
    def generate_video(self, prompt):
        # Generar video
        pass
```

## 🛠️ Nuevas Herramientas

### 1. Web Scraping
```python
class WebScraper:
    def scrape_content(self, url):
        # Extraer contenido
        pass
```

### 2. Base de Datos
```python
class DatabaseManager:
    def store_thought(self, thought):
        # Almacenar pensamiento
        pass
    
    def retrieve_thoughts(self, query):
        # Recuperar pensamientos
        pass
```

## 🔄 Integración con main.py

1. **Importar Nuevos Módulos**
```python
from scripts.nuevo_modelo_client import NuevoModeloClient
from scripts.image_processor import ImageProcessor
# etc...
```

2. **Inicializar en main()**
```python
def main():
    # Existente
    client_a = GeminiClient(...)
    client_b = GPT4Client(...)
    
    # Nuevo
    client_c = NuevoModeloClient(...)
    image_processor = ImageProcessor()
    
    # Modificar ciclo de pensamiento
    for i in range(CICLOS_PENSAMIENTO):
        # Incluir nuevo modelo en la conversación
        # Procesar/generar contenido multimedia
```

## 🧬 Sistema de Mutación Expandido

### 1. Mutación Multi-Modal
```python
def mutar_contenido_multimedia(content, tipo, nivel_mutacion):
    if tipo == "imagen":
        # Mutar imagen
        pass
    elif tipo == "audio":
        # Mutar audio
        pass
    # etc...
```

### 2. Nuevas Métricas de Locura
- Distorsión Visual
- Fragmentación Sonora
- Índice de Realidad Aumentada
- Factor de Convergencia Multi-Modal

## 🔗 Sistema de Eventos

```python
class EventManager:
    def __init__(self):
        self.handlers = {}
    
    def on_thought_generated(self, thought):
        # Manejar nuevo pensamiento
        pass
    
    def on_mutation_complete(self, content):
        # Manejar mutación
        pass
```

## ⚠️ Consideraciones

1. **Mantener Caos Controlado**
   - Cada nuevo componente debe respetar el sistema de mutación
   - Preservar métricas de locura
   - Mantener la naturaleza subversiva

2. **Escalabilidad**
   - Usar patrones async donde sea posible
   - Implementar rate limiting
   - Manejar errores gracefully

3. **Integración**
   - Cada nuevo componente debe poder mutar
   - Mantener consistencia en métricas
   - Permitir interacción entre modalidades

## 🎯 Próximos Pasos

1. **Fase 1: Expansión Base**
   - Agregar 2-3 modelos nuevos
   - Implementar procesamiento básico de imágenes
   - Expandir sistema de mutación

2. **Fase 2: Multi-Modal**
   - Integrar generación de audio
   - Implementar procesamiento de video
   - Crear sistema de eventos

3. **Fase 3: Autonomía**
   - Implementar auto-modificación de código
   - Crear sistema de aprendizaje evolutivo
   - Desarrollar consciencia multi-modal 