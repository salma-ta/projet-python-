import unittest
from datetime import datetime, timedelta
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from models import Client, Salle, Reservation
class TestClient(unittest.TestCase):
    def test_client_creation(self):
        client = Client(nom="Alice", email="alice@example.com")
        self.assertEqual(client.nom, "Alice")
        self.assertEqual(client.email, "alice@example.com")
        self.assertTrue(isinstance(client.id, str))
class TestSalle(unittest.TestCase):
    def test_salle_standard(self):
        salle=Salle(identifiant="12",type_salle="Standard",capacite=4)
        self.assertEqual(salle.identifiant, "12")
        self.assertEqual(salle.type_salle, "Standard")
        self.assertEqual(salle.capacite, 4)
    def test_salle_conference(self):
        salle=Salle(identifiant="3",type_salle="Conference",capacite=10)
        self.assertEqual(salle.identifiant, "3")
        self.assertEqual(salle.type_salle, "Conference")
        self.assertEqual(salle.capacite, 10)
    def test_salle_informatique(self):
        salle=Salle(identifiant="2",type_salle="Informatique",capacite=4)
        self.assertEqual(salle.identifiant, "2")
        self.assertEqual(salle.type_salle, "Informatique")
        self.assertEqual(salle.capacite, 4)
class TestReservation(unittest.TestCase):
    def test_reservation_duree_minimale(self):
        debut = datetime.now()
        fin = debut + timedelta(minutes=15)
        debut_str = debut.strftime("%Y-%m-%d %H:%M")
        fin_str = fin.strftime("%Y-%m-%d %H:%M")

        with self.assertRaises(ValueError):
            reservation=Reservation(client_id="123", identifiant="A", debut=debut_str, fin=fin_str)

    def test_reservation_valide(self):
        debut = datetime.now()
        fin = debut + timedelta(minutes=60)
        debut_str = debut.strftime("%Y-%m-%d %H:%M")
        fin_str = fin.strftime("%Y-%m-%d %H:%M")
        reservation = Reservation(client_id="123", identifiant="12", debut=debut_str, fin=fin_str)
        self.assertEqual(reservation.duree_minutes(), 60)
if __name__ == "__main__":
    unittest.main()