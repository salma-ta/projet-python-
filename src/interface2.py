import tkinter as tk
from tkinter import ttk, messagebox
from models import Client, Salle
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



def launch_app():
    root = tk.Tk()
    root.title("Gestion de réservation - MeetingPro")
    root.geometry("500x400")

    # Créer les onglets
    notebook = ttk.Notebook(root)
    notebook.pack(expand=True, fill='both')

    # Onglet Accueil
    accueil_frame = ttk.Frame(notebook)
    notebook.add(accueil_frame, text="Accueil")

    # Onglet Ajouter
    ajouter_frame = ttk.Frame(notebook)
    notebook.add(ajouter_frame, text="Ajouter")

    # Onglet Réserver
    reserver_frame = ttk.Frame(notebook)
    notebook.add(reserver_frame, text="Réserver")

    # Onglet Afficher
    afficher_frame = ttk.Frame(notebook)
    notebook.add(afficher_frame, text="Afficher")

    # Contenu de l'onglet Accueil (3 gros boutons)
    btn1 = tk.Button(accueil_frame, text="Ajouter", width=25, height=2, bg="#125873", fg="white", command=lambda: notebook.select(1))
    btn1.pack(pady=20)

    btn2 = tk.Button(accueil_frame, text="Réserver", width=25, height=2, bg="#125873", fg="white", command=lambda: notebook.select(2))
    btn2.pack(pady=20)

    btn3 = tk.Button(accueil_frame, text="Afficher", width=25, height=2, bg="#125873", fg="white", command=lambda: notebook.select(3))
    btn3.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    launch_app()
