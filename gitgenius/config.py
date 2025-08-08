import os
import json

CONFIG_FILE = os.path.join(os.path.expanduser("~"), ".gitgenius_config.json")

def load_config():
    """Load user config from file, default: emojis enabled."""
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)
    return {"emoji": True}  # default: emojis enabled

def save_config(config):
    """Save user config to file."""
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f, indent=4)
