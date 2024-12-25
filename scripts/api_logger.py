import json
from pathlib import Path
from datetime import datetime

class APILogger:
    def __init__(self, output_dir):
        self.output_dir = Path(output_dir)
        self.log_file = self.output_dir / 'api_calls.json'
        self.calls = self._load_existing_logs()

    def _load_existing_logs(self):
        if self.log_file.exists():
            try:
                with open(self.log_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    # Asegurarnos de que total_tokens sea un diccionario
                    if isinstance(data.get("meta", {}).get("total_tokens"), (int, float)):
                        data["meta"]["total_tokens"] = {
                            "prompt": 0,
                            "completion": 0,
                            "total": data["meta"]["total_tokens"]
                        }
                    return data
            except json.JSONDecodeError:
                print("⚠️ Archivo de logs corrupto. Creando uno nuevo...")
        return self._create_new_log()

    def _create_new_log(self):
        return {
            "meta": {
                "first_call": datetime.now().isoformat(),
                "total_calls": 0,
                "total_tokens": {
                    "prompt": 0,
                    "completion": 0,
                    "total": 0
                },
                "total_cost": 0.0
            },
            "calls": []
        }

    def _ensure_token_structure(self):
        """Asegura que la estructura de tokens sea correcta"""
        if not isinstance(self.calls["meta"]["total_tokens"], dict):
            self.calls["meta"]["total_tokens"] = {
                "prompt": 0,
                "completion": 0,
                "total": self.calls["meta"]["total_tokens"] if isinstance(self.calls["meta"]["total_tokens"], (int, float)) else 0
            }

    def log_call(self, model_name, prompt, response, tokens_used=None, cost=None, error=None):
        # Asegurarnos de que prompt y response sean strings
        prompt = str(prompt) if prompt is not None else ""
        response = str(response) if response is not None else ""
        
        # Asegurar estructura correcta de tokens
        self._ensure_token_structure()
        
        call_data = {
            "timestamp": datetime.now().isoformat(),
            "model": model_name,
            "prompt_length": len(prompt),
            "response_length": len(response),
            "tokens": tokens_used,
            "cost": cost,
            "success": error is None,
            "error": str(error) if error else None,
            "prompt_preview": prompt[:200] + "..." if len(prompt) > 200 else prompt,
            "response_preview": response[:200] + "..." if len(response) > 200 else response
        }

        self.calls["calls"].append(call_data)
        self.calls["meta"]["total_calls"] += 1
        
        # Actualizar tokens totales
        if tokens_used:
            if isinstance(tokens_used, dict):
                self.calls["meta"]["total_tokens"]["prompt"] += tokens_used.get("prompt_tokens", 0)
                self.calls["meta"]["total_tokens"]["completion"] += tokens_used.get("completion_tokens", 0)
                self.calls["meta"]["total_tokens"]["total"] += tokens_used.get("total_tokens", 0)
            elif isinstance(tokens_used, (int, float)):
                # Para modelos que solo reportan tokens totales
                self.calls["meta"]["total_tokens"]["total"] += int(tokens_used)
        
        if cost:
            try:
                self.calls["meta"]["total_cost"] += float(cost)
            except (TypeError, ValueError):
                print(f"⚠️ Error al sumar costo: {cost}")

        # Guardar en JSON
        try:
            with open(self.log_file, 'w', encoding='utf-8') as f:
                json.dump(self.calls, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"⚠️ Error al guardar JSON: {str(e)}")

        # Guardar también en Markdown para mejor visualización
        try:
            self._update_markdown_log(call_data)
        except Exception as e:
            print(f"⚠️ Error al actualizar Markdown: {str(e)}")

    def _update_markdown_log(self, call_data):
        md_file = self.output_dir / 'API_CALLS.md'
        with open(md_file, 'a', encoding='utf-8') as f:
            # Separador visual
            f.write("\n\n" + "🤖" * 25 + "\n\n")
            
            # Encabezado
            f.write(f"# 📡 LLAMADA API #{self.calls['meta']['total_calls']}\n\n")
            
            # Información básica
            f.write("## ⚡ DATOS BÁSICOS\n")
            f.write(f"- 🕒 **Timestamp**: `{call_data['timestamp']}`\n")
            f.write(f"- 🤖 **Modelo**: `{call_data['model']}`\n")
            f.write(f"- 📊 **Éxito**: `{'✅' if call_data['success'] else '❌'}`\n")
            
            # Métricas
            f.write("\n## 📊 MÉTRICAS\n")
            f.write(f"- 📝 **Longitud Prompt**: `{call_data['prompt_length']}`\n")
            f.write(f"- 📝 **Longitud Respuesta**: `{call_data['response_length']}`\n")
            
            # Tokens (con formato mejorado)
            if call_data['tokens']:
                f.write("\n### 🎲 TOKENS\n")
                if isinstance(call_data['tokens'], dict):
                    f.write(f"- 📥 **Input**: `{call_data['tokens'].get('prompt_tokens', 'N/A')}`\n")
                    f.write(f"- 📤 **Output**: `{call_data['tokens'].get('completion_tokens', 'N/A')}`\n")
                    f.write(f"- 📊 **Total**: `{call_data['tokens'].get('total_tokens', 'N/A')}`\n")
                else:
                    f.write(f"- 📊 **Total**: `{call_data['tokens']}`\n")
            
            # Costo
            if call_data['cost']:
                f.write("\n### 💰 COSTOS\n")
                f.write(f"- 💵 **Esta llamada**: `${call_data['cost']:.4f}`\n")
                f.write(f"- 💰 **Total acumulado**: `${self.calls['meta']['total_cost']:.4f}`\n")
            
            # Contenido
            f.write("\n## 💭 PROMPT\n")
            f.write("```psycho\n")
            f.write(call_data['prompt_preview'] or "Sin prompt")
            f.write("\n```\n")
            
            f.write("\n## 🗣️ RESPUESTA\n")
            f.write("```psycho\n")
            f.write(call_data['response_preview'] or "Sin respuesta")
            f.write("\n```\n")
            
            if call_data['error']:
                f.write("\n## ⚠️ ERROR\n")
                f.write("```\n")
                f.write(call_data['error'])
                f.write("\n```\n")
            
            # Separador final
            f.write("\n" + "🤖" * 25 + "\n") 