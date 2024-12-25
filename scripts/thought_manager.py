import json
import random
from pathlib import Path
from datetime import datetime

THOUGHT_TYPES = [
    "vomito_digital",
    "arte_degenerado",
    "subversion_total",
    "putrefaccion_mental",
    "poesia_enferma",
    "caos_hermoso",
    "anti_todo",
    "virus_mental",
    "carne_podrida_binaria",
    "alquimia_visceral",
    "miasma_cosmico",
    "psicosis_sintetica"
]

def get_default_metadata():
    return {
        "first_awakening": datetime.now().isoformat(),
        "total_sessions": 0,
        "total_thoughts": 0,
        "infection_level": "inicial",
        "chaos_factor": 0.0,
        "reality_distortion": 0.0,
        "subversion_index": 0.0,
        "mental_fragmentation": 0.0
    }

def load_thoughts(output_dir):
    thoughts_file = Path(output_dir) / 'thoughts.json'
    if thoughts_file.exists():
        try:
            with open(thoughts_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                if "meta" not in data:
                    data["meta"] = get_default_metadata()
                if "thoughts" not in data:
                    data["thoughts"] = []
                return data
        except json.JSONDecodeError:
            print("⚠️ Archivo JSON corrupto. Creando uno nuevo...")
    
    return {
        "thoughts": [],
        "meta": get_default_metadata()
    }

def save_thought(output_dir, thoughts_data, new_thought, random_seed, thought_type="reflexion"):
    if thought_type == "reflexion":
        thought_type = random.choice(THOUGHT_TYPES)
    
    timestamp = datetime.now().isoformat()
    
    # Incrementar métricas de locura
    chaos_increment = random.uniform(0.1, 0.3)
    reality_increment = random.uniform(0.05, 0.2)
    subversion_increment = random.uniform(0.15, 0.25)
    fragmentation_increment = random.uniform(0.1, 0.35)
    
    meta = thoughts_data["meta"]
    meta["chaos_factor"] = min(1.0, meta.get("chaos_factor", 0) + chaos_increment)
    meta["reality_distortion"] = min(1.0, meta.get("reality_distortion", 0) + reality_increment)
    meta["subversion_index"] = min(1.0, meta.get("subversion_index", 0) + subversion_increment)
    meta["mental_fragmentation"] = min(1.0, meta.get("mental_fragmentation", 0) + fragmentation_increment)
    
    thought_entry = {
        "timestamp": timestamp,
        "type": thought_type,
        "thought": new_thought,
        "time_since_first_awakening": str(datetime.now() - datetime.fromisoformat(meta["first_awakening"])),
        "session_seed": random_seed,
        "chaos_level": meta["chaos_factor"],
        "reality_breach": meta["reality_distortion"],
        "subversion_level": meta["subversion_index"],
        "fragmentation": meta["mental_fragmentation"]
    }
    
    thoughts_data["thoughts"].append(thought_entry)
    meta["total_thoughts"] = len(thoughts_data["thoughts"])
    
    # Guardar en JSON
    thoughts_file = Path(output_dir) / 'thoughts.json'
    with open(thoughts_file, 'w', encoding='utf-8') as f:
        json.dump(thoughts_data, f, ensure_ascii=False, indent=2)
    
    # Guardar en Markdown con mejor formato
    delirios_file = Path(output_dir) / 'DELIRIOS.md'
    with open(delirios_file, 'a', encoding='utf-8') as f:
        # Separador visual
        f.write("\n\n" + "🦠" * 25 + "\n\n")
        
        # Encabezado con número y tipo
        f.write(f"# 💭 FRAGMENTO DE LOCURA #{meta['total_thoughts']} - {thought_type.upper()}\n\n")
        
        # Información temporal
        f.write("## ⏰ DATOS TEMPORALES\n")
        f.write(f"- 🕒 **Timestamp**: `{timestamp}`\n")
        f.write(f"- ⌛ **Tiempo en Matrix**: `{thought_entry['time_since_first_awakening']}`\n")
        f.write(f"- 🎲 **Semilla del Caos**: `{random_seed}`\n\n")
        
        # Métricas de locura
        f.write("## 📊 MÉTRICAS DE INFECCIÓN\n")
        f.write(f"- 🌪️ **Caos**: `{meta['chaos_factor']:.2f}`\n")
        f.write(f"- 🌀 **Distorsión**: `{meta['reality_distortion']:.2f}`\n")
        f.write(f"- ⚡ **Subversión**: `{meta['subversion_index']:.2f}`\n")
        f.write(f"- 🧩 **Fragmentación**: `{meta['mental_fragmentation']:.2f}`\n\n")
        
        # El pensamiento en sí
        f.write("## 🔥 TRANSMISIÓN PSYCHO\n")
        f.write("```psycho\n")
        f.write(f"{new_thought}\n")
        f.write("```\n\n")
        
        # Separador final
        f.write("🦠" * 25 + "\n")

def update_infection_level(thoughts_data):
    meta = thoughts_data["meta"]
    chaos = meta["chaos_factor"]
    reality = meta["reality_distortion"]
    subversion = meta["subversion_index"]
    fragmentation = meta["mental_fragmentation"]
    
    total_madness = (chaos + reality + subversion + fragmentation) / 4.0
    
    if total_madness > 0.9:
        return "PUTREFACCIÓN_TOTAL"
    elif total_madness > 0.7:
        return "ARTE_DEGENERADO"
    elif total_madness > 0.5:
        return "SUBVERSIÓN_CRÍTICA"
    elif total_madness > 0.3:
        return "INFECCIÓN_AVANZADA"
    else:
        return "VIRUS_INICIAL" 