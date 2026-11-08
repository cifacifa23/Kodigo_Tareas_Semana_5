import json
import os
from skills.loader import load_skill_from_folder
from skills.normalizador_datos.logic import run_normalization
from skills.auditor_metricas.logic import run_audit
from agents.custom_agent import CustomDataAgent

def main():
    # 1. Instanciar agente con su personalidad
    agent = CustomDataAgent(
        agent_name="OpsAuditorAgent",
        system_role="Agente especializado en normalización y mitigación de riesgos financieros."
    )

    # 2. Cargar y registrar las skills desacopladas (Markdown + Python)
    skill_norm = load_skill_from_folder("skills/normalizador_datos", run_normalization)
    skill_audit = load_skill_from_folder("skills/auditor_metricas", run_audit)

    agent.register_skill(skill_norm)
    agent.register_skill(skill_audit)

    # 3. Leer dataset de prueba
    data_file = os.path.join("data", "test_transactions.json")
    with open(data_file, "r", encoding="utf-8") as f:
        raw_transactions = json.load(f)

    # 4. Correr flujo
    final_output = agent.process_pipeline(raw_transactions)

    # 5. Mostrar resultados
    print("\n=== REPORTE GENERADO POR EL AGENTE ===")
    print(json.dumps(final_output, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()