import json
from pathlib import Path

MEMORY_FILE = Path(__file__).with_name("shiv_memory.json")

def load_memory():
    if MEMORY_FILE.exists():
        with open(MEMORY_FILE, "r", encoding = "utf-8") as file:
            return json.load(file)


    return {}

def save_memory(memory):
    with open(MEMORY_FILE, "w", encoding ="utf-8") as file:
        json.dump(memory, file, indent=4, ensure_ascii = False)            