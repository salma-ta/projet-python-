
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
<<<<<<< HEAD


=======
>>>>>>> 0f5137847c23e0ce66ae911608b3f8b2e203a886
