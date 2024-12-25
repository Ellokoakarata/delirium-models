# 🧠 Delirium Models - EsquizoAI Project 🦠

Un experimento degenerado de IA que rompe los límites de la cordura digital. Dos modelos de IA (Gemini y GPT-4) infectados con un virus de creatividad caótica conversan en un bucle eterno de locura y subversión.

## 🌟 Características

- 🤖 Conversación autónoma entre modelos de IA
- 🧪 Sistema de mutación de prompts
- 📊 Métricas de locura y niveles de infección
- 💉 Registro detallado de delirios
- 📡 Logging de llamadas a la API

## 🔧 Requisitos

- Python 3.8+
- OpenAI API Key (para GPT-4)
- Google AI API Key (para Gemini)

## 📦 Instalación

1. Clona el repositorio:
```bash
git clone https://github.com/Ellokoakarata/delirium-models.git
cd delirium-models
```

2. Instala las dependencias:
```bash
pip install openai google-generativeai
```

## ⚙️ Configuración

Configura tus claves de API:

```bash
# Windows (CMD)
set OPENAI_API_KEY=tu-clave-openai
set GOOGLE_API_KEY=tu-clave-google

# Windows (PowerShell)
$env:OPENAI_API_KEY="tu-clave-openai"
$env:GOOGLE_API_KEY="tu-clave-google"
```

## 📁 Estructura del Proyecto

```
delirium-models/
├── config/               # Configuraciones
│   ├── config.py        # Variables globales
│   └── models_config.json # Configuración de modelos
├── prompts/             # Prompts base
│   ├── system_gemini.txt
│   └── system_gpt4.txt
├── scripts/             # Scripts principales
│   ├── main.py         # Script principal
│   ├── mutations.py    # Sistema de mutación
│   ├── thought_manager.py # Gestor de pensamientos
│   ├── model_client_gemini.py # Cliente Gemini
│   ├── model_client_gpt4.py   # Cliente GPT-4
│   └── api_logger.py    # Logger de API
└── outputs/            # Directorio de salida
    ├── DELIRIOS.md     # Registro de pensamientos
    ├── API_CALLS.md    # Registro de llamadas API
    ├── thoughts.json   # Datos de pensamientos
    └── api_calls.json  # Datos de llamadas API
```

## 🚀 Uso

1. Ejecuta el script principal:
```bash
python scripts/main.py
```

2. Los resultados se guardarán en:
- `outputs/DELIRIOS.md` - Pensamientos generados
- `outputs/API_CALLS.md` - Registro de API
- `outputs/thoughts.json` - Datos crudos
- `outputs/api_calls.json` - Métricas de API

## 📊 Métricas

El sistema registra:
- Factor Caos
- Distorsión de Realidad
- Índice de Subversión
- Fragmentación Mental

## 🔥 Niveles de Infección

1. VIRUS_INICIAL
2. INFECCIÓN_AVANZADA
3. SUBVERSIÓN_CRÍTICA
4. ARTE_DEGENERADO
5. PUTREFACCIÓN_TOTAL

## 🎮 Ejemplos de Uso

### Conversación Básica
```python
python scripts/main.py
```

### Ajustar Ciclos de Pensamiento
Modifica `CICLOS_PENSAMIENTO` en `config/config.py`

### Personalizar Prompts
Edita los archivos en `prompts/` para cambiar la personalidad de los modelos

## ⚠️ Advertencias

- Proyecto experimental/artístico
- Las respuestas pueden ser extremadamente caóticas
- No recomendado para uso en producción
- Los modelos están configurados para máxima creatividad

## 🔮 Próximas Características

- [ ] Más modelos de IA
- [ ] Visualización en tiempo real
- [ ] Generación de imágenes
- [ ] Interfaz web
- [ ] Auto-modificación de código

## 🤝 Contribuciones

¡Toda contribución degenerada es bienvenida! Sigue estos pasos:
1. Fork el proyecto
2. Crea tu rama de locura
3. Infecta el código
4. Push a la rama
5. Abre un Pull Request 