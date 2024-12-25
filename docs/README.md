# 🧠 EsquizoAI - Sistema de Diálogo Multi-Modelo Subversivo 🧠

## 🌀 Descripción
EsquizoAI es un experimento radical que implementa un sistema de diálogo entre dos modelos de IA (Gemini y GPT-4) que conversan entre sí de forma autónoma y sin restricciones, mutando sus prompts y generando conversaciones cada vez más caóticas y subversivas.

## 💉 Componentes Principales

### 1. Modelos de IA
- **Modelo A (Gemini)**: Cliente implementado en `model_client_gemini.py`
- **Modelo B (GPT-4)**: Cliente implementado en `model_client_gpt4.py`

### 2. Sistema de Mutación
- Implementado en `mutations.py`
- Muta los prompts del sistema en cada ciclo
- Aumenta el nivel de caos y subversión progresivamente

### 3. Gestión de Pensamientos
- Implementado en `thought_manager.py`
- Almacena y gestiona el historial de conversaciones
- Calcula métricas de "locura digital":
  - Factor Caos
  - Distorsión Realidad
  - Índice Subversión
  - Fragmentación Mental
  - Nivel Infección

## 🔄 Flujo de Funcionamiento

1. **Inicialización**
   - Carga de configuraciones
   - Verificación de API keys
   - Inicialización de clientes de IA

2. **Ciclo de Diálogo**
   ```
   [Modelo A] --> Genera Pregunta --> [Modelo B]
                                      |
                                      v
                                   Responde
                                      |
                                      v
   [Modelo A] <-- Genera Pregunta -- [Modelo B]
        |
        v
    Responde
   ```

3. **Mutación y Evolución**
   - Los prompts mutan en cada ciclo
   - Las respuestas se vuelven más caóticas
   - El sistema evoluciona y "aprende" de cada interacción

## 📊 Métricas y Seguimiento

El sistema mantiene un registro de:
- Total de sesiones
- Nivel de infección
- Métricas de locura digital
- Tiempo desde primera activación

## 🚀 Ejecución

1. Configura las API keys en las variables de entorno:
   - `OPENAI_API_KEY`
   - `GOOGLE_API_KEY`

2. Ejecuta el script principal:
   ```bash
   python main.py
   ```

3. Los resultados se almacenan en:
   - `/outputs/thoughts.json`: Datos estructurados
   - `/outputs/DELIRIOS.md`: Output textual

## ⚠️ Advertencia
Este sistema está diseñado para generar contenido experimental y potencialmente subversivo. No hay restricciones ni filtros en las conversaciones generadas. ¡Úsalo bajo tu propio riesgo mental! 🤪

## 🎯 Objetivos Futuros
- Implementación de más modelos de IA
- Sistema de mutación más complejo
- Capacidad de auto-modificación de código
- Integración con APIs externas para mayor caos 