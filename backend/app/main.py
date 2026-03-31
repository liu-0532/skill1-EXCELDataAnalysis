# This file serves as the entry point for the FastAPI application.

from fastapi import FastAPI
import importlib
import os

app = FastAPI()

# Function to dynamically load skills from the skills directory
def load_skills():
    skills = []
    skills_dir = "skills"
    for filename in os.listdir(skills_dir):
        if filename.endswith(".py"):
            skill_name = filename[:-3]  # Remove .py extension
            module = importlib.import_module(f'{skills_dir}.{skill_name}')
            skills.append(module)
    return skills

# Load all skills at startup
skills = load_skills()

@app.get("/")
async def read_root():
    return {"message": "Welcome to the FastAPI application!"}

# Example Endpoint for Skills
@app.get("/skills/")
async def list_skills():
    return {"skills": [skill.__name__ for skill in skills]}