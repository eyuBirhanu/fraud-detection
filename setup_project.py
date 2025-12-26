import os

# Define the folder structure
folders = [
    ".vscode",
    ".github/workflows",
    "data/raw",
    "data/processed",
    "notebooks",
    "src",
    "tests",
    "models",
    "scripts"
]

# Define the files to create
files = [
    ".gitignore",
    "requirements.txt",
    "README.md",
    "src/__init__.py",
    "src/preprocess.py",
    "src/modeling.py",
    "scripts/__init__.py",
    "notebooks/__init__.py",
    "tests/__init__.py"
]

# Create Folders
for folder in folders:
    try:
        os.makedirs(folder, exist_ok=True)
        print(f"Created folder: {folder}")
    except Exception as e:
        print(f"Error creating {folder}: {e}")

# Create Files
for file in files:
    try:
        with open(file, 'w') as f:
            pass # Create empty file
        print(f"Created file: {file}")
    except Exception as e:
        print(f"Error creating {file}: {e}")

print("\nProject structure set up successfully!")