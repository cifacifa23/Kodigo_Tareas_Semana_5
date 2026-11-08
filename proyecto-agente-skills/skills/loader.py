import os
import frontmatter
from typing import Callable, Dict, Any

class SkillDefinition:
    def __init__(self, name: str, description: str, instructions: str, execute_fn: Callable):
        self.name = name
        self.description = description
        self.instructions = instructions
        self.execute_fn = execute_fn

    def run(self, **kwargs) -> Any:
        return self.execute_fn(**kwargs)

def load_skill_from_folder(skill_folder_path: str, logic_function: Callable) -> SkillDefinition:
    skill_md_path = os.path.join(skill_folder_path, "skill.md")
    
    if not os.path.exists(skill_md_path):
        raise FileNotFoundError(f"No se encontró skill.md en {skill_folder_path}")

    with open(skill_md_path, "r", encoding="utf-8") as f:
        parsed = frontmatter.load(f)

    return SkillDefinition(
        name=parsed.metadata.get("name", os.path.basename(skill_folder_path)),
        description=parsed.metadata.get("description", ""),
        instructions=parsed.content,
        execute_fn=logic_function
    )