import os

# Define project structure
structure = {
    "fastapi_agent_project": {
        "app": {
            "auth": {
                "routes.py": "",
                "models.py": "",
                "schemas.py": "",
                "utils.py": ""
            },
            "agents": {
                "agent_manager.py": "",
                "tools.py": "",
                "memory.py": ""
            },
            "chats": {
                "routes.py": "",
                "models.py": "",
                "schemas.py": "",
                "service.py": ""
            },
            "documents": {
                "routes.py": "",
                "models.py": "",
                "service.py": ""
            },
            "utils": {
                "deps.py": ""
            },
            "alembic": {},
            "tests": {},
            "main.py": "",
            "config.py": "",
            "db.py": ""
        },
        "requirements.txt": "",
        "alembic.ini": "",
        "Dockerfile": "",
        "docker-compose.yml": "",
        "README.md": ""
    }
}

def create_structure(base_path, structure_dict):
    for name, content in structure_dict.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):  # Directory
            os.makedirs(path, exist_ok=True)
            create_structure(path, content)
        else:  # File
            with open(path, "w") as f:
                if path.endswith("README.md"):
                    f.write("# FastAPI Agent Project\n")
                elif path.endswith("requirements.txt"):
                    f.write("fastapi\nuvicorn\nsqlalchemy\npsycopg2-binary\nalembic\nlangchain\npgvector\npython-jose\npasslib[bcrypt]\n")
                elif path.endswith("docker-compose.yml"):
                    f.write("version: '3.8'\nservices:\n  api:\n    build: .\n    ports:\n      - '8000:8000'\n    depends_on:\n      - db\n  db:\n    image: postgres:15\n    environment:\n      POSTGRES_USER: user\n      POSTGRES_PASSWORD: password\n      POSTGRES_DB: fastapi_db\n    ports:\n      - '5432:5432'\n")
                elif path.endswith("Dockerfile"):
                    f.write("FROM python:3.11-slim\nWORKDIR /app\nCOPY requirements.txt .\nRUN pip install --no-cache-dir -r requirements.txt\nCOPY . .\nCMD [\"uvicorn\", \"app.main:app\", \"--host\", \"0.0.0.0\", \"--port\", \"8000\"]\n")
                else:
                    f.write("")

# Run script in current folder
base_dir = os.getcwd()  # current working dir (ai-research-assistant-api)
create_structure(base_dir, structure)

print("✅ fastapi_agent_project structure created successfully!")
