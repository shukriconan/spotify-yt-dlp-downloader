import json
import os

CONFIG_PATH = "config.json"

def load_config():
    if not os.path.exists(CONFIG_PATH):
        raise FileNotFoundError(f"Config file {CONFIG_PATH} not found.")
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        return json.load(f)
