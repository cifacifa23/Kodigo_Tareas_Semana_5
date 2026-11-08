from typing import Dict, Any, List
from skills.loader import SkillDefinition

class CustomDataAgent:
    def __init__(self, agent_name: str, system_role: str):
        self.name = agent_name
        self.system_role = system_role
        self.skills: Dict[str, SkillDefinition] = {}

    def register_skill(self, skill: SkillDefinition) -> None:
        self.skills[skill.name] = skill
        print(f"[{self.name}] Skill registrada con éxito: '{skill.name}'")

    def execute_skill(self, skill_name: str, **kwargs) -> Any:
        if skill_name not in self.skills:
            raise KeyError(f"La skill '{skill_name}' no existe en este agente.")
        return self.skills[skill_name].run(**kwargs)

    def process_pipeline(self, raw_data: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Ejecuta el ciclo de vida del agente usando sus skills registradas."""
        print(f"\n--- Iniciando procesamiento con {self.name} ---")

        # 1. Ejecutar skill de normalización
        normalized_data = self.execute_skill("transaction-data-normalizer", records=raw_data)

        # 2. Ejecutar skill de auditoría sobre datos limpios
        audit_report = self.execute_skill("transaction-anomaly-auditor", records=normalized_data, threshold=1000.0)

        # 3. Respuesta estructurada del agente
        return {
            "agent_name": self.name,
            "role": self.system_role,
            "normalized_data": normalized_data,
            "audit_summary": audit_report
        }