import json
import logging
from pathlib import Path

def export_to_json(data, filepath: Path):
    filepath.parent.mkdir(parents=True, exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    logging.info(f"Exported data to {filepath}")