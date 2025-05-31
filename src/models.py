import uuid
#model#
class Client:
    def __init__(self, nom, email):
        self.nom = nom
        self.email = email
        self.id = str(uuid.uuid4())

    def __repr__(self):
        return f"Client({self.nom}, {self.email}, {self.id})"

class Salle:
    def __init__(self, identifiant, type_salle, capacite):
        self.identifiant = identifiant
        self.type_salle = type_salle  #  'conference', 'informatique'
        self.capacite = capacite

    def __repr__(self):
        return f"Salle({self.identifiant}, {self.type_salle}, {self.capacite})"

from datetime import datetime

class Reservation:
    DUREE_MINIMALE_MINUTES = 30
    def __init__(self, client_id, identifiant, debut, fin):
        self.client_id = client_id
        self.identifiant = identifiant
        self.debut = datetime.strptime(debut, "%Y-%m-%d %H:%M")
        self.fin = datetime.strptime(fin, "%Y-%m-%d %H:%M")
        if self.duree_minutes() < Reservation.DUREE_MINIMALE_MINUTES:
            raise ValueError(f"La durée minimale d'une réservation est de {Reservation.DUREE_MINIMALE_MINUTES} minutes")
    def duree_minutes(self):
        return int((self.fin - self.debut).total_seconds() / 60)

    def __repr__(self):
        return f"Reservation({self.client_id}, {self.nom_salle}, {self.debut}, {self.fin})"
