import json
from pathlib import Path


DATA_FILE = Path(__file__).with_name("data.json")


DEFAULT_DATA = {
    "students": [],
    "classes": [],
    "enrollments": [],
    "next_ids": {
        "student": 1,
        "class": 1,
        "enrollment": 1,
    },
}


def load_data():
    if not DATA_FILE.exists():
        save_data(DEFAULT_DATA)
        return json.loads(json.dumps(DEFAULT_DATA))

    with DATA_FILE.open("r", encoding="utf-8") as file:
        data = json.load(file)

    return ensure_structure(data)


def save_data(data):
    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)


def ensure_structure(data):
    merged = json.loads(json.dumps(DEFAULT_DATA))
    merged.update({k: v for k, v in data.items() if k in merged})

    next_ids = merged["next_ids"]
    incoming_ids = data.get("next_ids", {})
    next_ids.update({k: v for k, v in incoming_ids.items() if k in next_ids})

    return merged
