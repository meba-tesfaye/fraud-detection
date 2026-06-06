import os

# Define the folder structure required by the project specifications
dirs = [
    "data/raw",
    "data/processed",
    "notebooks",
    "src",
    "tests",
    "models",
    "scripts",
    ".vscode",
    ".github/workflows"
]

for d in dirs:
    os.makedirs(d, exist_ok=True)
    # Create empty __init__.py files for internal module paths where needed
    if d in ["notebooks", "src", "tests", "scripts"]:
        with open(os.path.join(d, "__init__.py"), "w") as f:
            pass

# Create an initial .gitignore to ensure data files are never accidentally pushed to GitHub
gitignore_content = """\
data/raw/*
data/processed/*
models/*
.env
__pycache__/
*.pyc
.ipynb_checkpoints/
"""

with open(".gitignore", "w") as f:
    f.write(gitignore_content)

print("✅ Professional repository structure successfully scaffolded!")