import tkinter as tk
from tkinter import messagebox

from models import Client     
#from models import Salle 
from database import load_data, save_data


def ajouter_salle_ui():
    # Fenêtre simplifiée pour ajouter une salle
    popup = tk.Toplevel()
    popup.title("Ajouter une salle")
    
    tk.Label(popup, text="Type de salle:").pack()
    type_salle = tk.Entry(popup)
    type_salle.pack()
    
    tk.Label(popup, text="Capacité:").pack()
    capacite = tk.Entry(popup)
    capacite.pack()

    def valider():
        # Validation basique
        if type_salle.get() and capacite.get():
            messagebox.showinfo("Succès", "Salle ajoutée")
            popup.destroy()
    
    tk.Button(popup, text="Valider", command=valider).pack(pady=10)

# Fenêtre principale 
def launch_app():
    root = tk.Tk()
    root.title("Gestion de réservation - MeetingPro")
    root.geometry("400x300")

    # Boutons principaux 
    btn_client = tk.Button(root, text="Ajouter un client", width=30, command=ajouter_client_ui)
    btn_client.pack(pady=10)

    btn_salle = tk.Button(root, text="Ajouter une salle", width=30, command=ajouter_salle_ui) # type: ignore
    btn_salle.pack(pady=10)

    root.mainloop()

# Fenêtre pour ajouter un client
def ajouter_client_ui():
    window = tk.Toplevel()
    window.title("Ajouter un client")

    tk.Label(window, text="Nom :").pack()
    entry_nom = tk.Entry(window)
    entry_nom.pack()

    tk.Label(window, text="Email :").pack()
    entry_email = tk.Entry(window)
    entry_email.pack()

    def enregistrer():
        nom = entry_nom.get()
        email = entry_email.get()
        client = Client(nom, email)
        data = load_data("data.json")
        data["clients"].append(client.__dict__)
        save_data("data.json", data)
        messagebox.showinfo("Succès", "Client ajouté avec succès.")
        window.destroy()

    tk.Button(window, text="Enregistrer", command=enregistrer).pack(pady=10)

if __name__ == "__main__":
    launch_app()
    

    
