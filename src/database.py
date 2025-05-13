
import json

def load_data(filename):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"clients": [], "salles": [], "reservations": []}

def save_data(filename, data):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
