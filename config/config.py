import os

# Claves de API
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")

# Ajustes globales
DEFAULT_TEMPERATURE = 0.99
DEFAULT_MAX_TOKENS = 4096

# Rutas
PROMPTS_DIR = "prompts/"
OUTPUT_DIR = "outputs/"

# Parámetros del ciclo de pensamiento
CICLOS_PENSAMIENTO = 3 