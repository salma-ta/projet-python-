import uuid

class Client:
    def __init__(self, nom, email):
        self.nom = nom
        self.email = email
        self.id = str(uuid.uuid4())

    def __repr__(self):
        return f"Client({self.nom}, {self.email}, {self.id})"

class Salle:
    def __init__(self, nom, type_salle, capacite):
        self.nom = nom
        self.type_salle = type_salle  # 'standard', 'conference', 'informatique'
        self.capacite = capacite

    def __repr__(self):
        return f"Salle({self.nom}, {self.type_salle}, {self.capacite})"

from datetime import datetime

class Reservation:
    def __init__(self, client_id, nom_salle, debut, fin):
        self.client_id = client_id
        self.nom_salle = nom_salle
        self.debut = datetime.strptime(debut, "%Y-%m-%d %H:%M")
        self.fin = datetime.strptime(fin, "%Y-%m-%d %H:%M")

    def __repr__(self):
        return f"Reservation({self.client_id}, {self.nom_salle}, {self.debut}, {self.fin})"
