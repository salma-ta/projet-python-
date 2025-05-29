import tkinter as tk
from tkinter import ttk, messagebox
class Meetingproapp :
    def __init__(self,root):
        self.root=root
        self.root.title('Meetingproapp')
        self.onglets=ttk.Onglets(self,root)
        self.onglets.pack(fill='both', expand=True)
        self.accueil_tab = ttk.Frame(self.onglets)
        self.onglets.add(self.accueil_tab, text="Accueil")
        self.onglets.add(self.accueil_tab, text="Ajouter")
        self.onglets.add(self.accueil_tab, text="Afficher")
        self.onglets.add(self.accueil_tab, text="Réserver")

        pass