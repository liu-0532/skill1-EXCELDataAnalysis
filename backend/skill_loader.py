import os
import importlib

class SkillLoader:
    def __init__(self, skills_directory):
        self.skills_directory = skills_directory
        self.skills = {}

    def load_skills(self):
        # Iterate over all Python files in the skills directory
        for filename in os.listdir(self.skills_directory):
            if filename.endswith('.py'):
                skill_name = filename[:-3]  # Remove .py extension
                module_path = f"{self.skills_directory.replace('/', '.')}.{skill_name}"

                # Dynamically import the skill module
                module = importlib.import_module(module_path)
                self.skills[skill_name] = module  # Store the imported module

    def get_skills(self):
        return self.skills
