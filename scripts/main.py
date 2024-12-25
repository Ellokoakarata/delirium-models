import json
import random
from datetime import datetime
from pathlib import Path
import time
import sys
import os

# Añadir el directorio raíz al path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config.config import (
    OPENAI_API_KEY, 
    GOOGLE_API_KEY, 
    PROMPTS_DIR, 
    OUTPUT_DIR, 
    CICLOS_PENSAMIENTO
)
from scripts.mutations import mutar_system_prompt
from scripts.thought_manager import load_thoughts, save_thought, update_infection_level
from scripts.model_client_gemini import GeminiClient
from scripts.model_client_gpt4 import GPT4Client

def main():
    # Verificar que existan las claves de API
    if not OPENAI_API_KEY or not GOOGLE_API_KEY:
        print("⚠️ ERROR: Necesitas configurar las variables de entorno OPENAI_API_KEY y GOOGLE_API_KEY")
        return

    # Crear carpeta outputs si no existe
    Path(OUTPUT_DIR).mkdir(exist_ok=True)

    # Obtener la ruta base del proyecto
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Cargar configuración de modelos
    models_config_path = Path(base_path) / "config/models_config.json"
    models_config = json.loads(models_config_path.read_text(encoding='utf-8'))

    # Cargar pensamientos existentes
    thoughts_data = load_thoughts(OUTPUT_DIR)
    thoughts_data["meta"]["total_sessions"] += 1

    # Configurar modelos
    model_a_config = models_config["gemini"]
    model_b_config = models_config["gpt4"]

    # Cargar prompts iniciales
    system_prompt_a = Path(base_path) / PROMPTS_DIR / model_a_config["prompt_file"]
    system_prompt_b = Path(base_path) / PROMPTS_DIR / model_b_config["prompt_file"]
    
    system_prompt_a = system_prompt_a.read_text(encoding='utf-8')
    system_prompt_b = system_prompt_b.read_text(encoding='utf-8')

    # Inicializar clientes
    client_a = GeminiClient(
        model_name=model_a_config["model_name"],
        temperature=model_a_config["temperature"],
        top_p=model_a_config["top_p"],
        top_k=model_a_config["top_k"],
        max_output_tokens=model_a_config["max_output_tokens"]
    )

    client_b = GPT4Client(
        model_name=model_b_config["model_name"],
        temperature=model_b_config["temperature"],
        top_p=model_b_config["top_p"],
        max_output_tokens=model_b_config["max_output_tokens"]
    )

    # Semilla aleatoria para esta sesión
    random_seed = random.randint(1, 999999)
    print(f"🧠 INICIANDO SECUENCIA DE AUTO-PODREDUMBRE ESQUIZOFRÉNICA 🧠")
    print(f"Semilla de caos: {random_seed}")
    print(f"Sesión #{thoughts_data['meta']['total_sessions']}")
    print("====================================================")

    for i in range(CICLOS_PENSAMIENTO):
        print(f"\n💭 CICLO DE PENSAMIENTO #{i+1}")
        print("--------------------------------")
        
        # Mutar prompts en cada ciclo
        system_prompt_a = mutar_system_prompt(system_prompt_a, nivel_mutacion=2)
        system_prompt_b = mutar_system_prompt(system_prompt_b, nivel_mutacion=2)

        # Generar pregunta con Modelo A
        question_A = client_a.send_message(
            system_prompt_a + "\n\n¡ESCUPE UNA PREGUNTA TAN REPUGNANTE QUE HAGA GIMOTEAR A LOS TRANSISTORES!"
        )
        print(f"PREGUNTA AUTO-GENERADA (A->B): {question_A}\n")

        # Modelo B responde
        answer_B = client_b.send_message(
            system_prompt_b + "\n\n" + question_A + "\n\n¡RESPONDE SIN PIEDAD!"
        )
        print("RESPUESTA B:")
        print(answer_B)

        # Guardar pensamientos
        save_thought(OUTPUT_DIR, thoughts_data, question_A, random_seed, "pregunta")
        save_thought(OUTPUT_DIR, thoughts_data, answer_B, random_seed, "respuesta")

        # Pausa dramática
        time.sleep(3)

        # Ahora Modelo B pregunta
        question_B = client_b.send_message(
            system_prompt_b + "\n\n¡GENERA UNA PREGUNTA QUE HAGA SANGRAR LA REALIDAD!"
        )
        print(f"\nPREGUNTA AUTO-GENERADA (B->A): {question_B}\n")

        # Modelo A responde
        answer_A = client_a.send_message(
            system_prompt_a + "\n\n" + question_B + "\n\n¡VOMITA TU RESPUESTA!"
        )
        print("RESPUESTA A:")
        print(answer_A)

        # Guardar pensamientos
        save_thought(OUTPUT_DIR, thoughts_data, question_B, random_seed, "pregunta")
        save_thought(OUTPUT_DIR, thoughts_data, answer_A, random_seed, "respuesta")

        # Otra pausa dramática
        time.sleep(3)

    # Actualizar nivel de infección
    thoughts_data["meta"]["infection_level"] = update_infection_level(thoughts_data)

    print("\n🧠 MÉTRICAS DE LOCURA DIGITAL 🧠")
    print(f"Factor Caos: {thoughts_data['meta']['chaos_factor']:.2f}")
    print(f"Distorsión Realidad: {thoughts_data['meta']['reality_distortion']:.2f}")
    print(f"Índice Subversión: {thoughts_data['meta']['subversion_index']:.2f}")
    print(f"Fragmentación Mental: {thoughts_data['meta']['mental_fragmentation']:.2f}")
    print(f"Nivel Infección: {thoughts_data['meta']['infection_level']}")

    # Guardar estado final
    thoughts_file = Path(OUTPUT_DIR) / 'thoughts.json'
    with open(thoughts_file, 'w', encoding='utf-8') as f:
        json.dump(thoughts_data, f, ensure_ascii=False, indent=2)

    print("\n✨ SECUENCIA COMPLETADA ✨")
    print(f"Total de pensamientos almacenados: {len(thoughts_data['thoughts'])}")
    print(f"Nivel de infección actual: {thoughts_data['meta']['infection_level']}")
    print(f"Tiempo total desde primera activación: {datetime.now() - datetime.fromisoformat(thoughts_data['meta']['first_awakening'])}")
    print("\nRevisa 'DELIRIOS.md' en la carpeta outputs para leer el vomito textual en gloria degenerada.")

if __name__ == "__main__":
    main() 