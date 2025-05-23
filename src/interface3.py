import tkinter as tk
from tkinter import ttk, messagebox
from models import Client, Salle
from database import load_data, save_data

# === Fenêtre pour ajouter une salle ===
def ajouter_salle_ui():
    popup = tk.Toplevel()
    popup.title("Ajouter une salle")

    tk.Label(popup, text="Type de salle:").pack()
    type_salle = tk.Entry(popup)
    type_salle.pack()

    tk.Label(popup, text="Capacité:").pack()
    capacite = tk.Entry(popup)
    capacite.pack()

    def valider():
        if type_salle.get() and capacite.get().isdigit():
            salle = Salle(type_salle.get(), int(capacite.get()))
            data = load_data("data.json")
            data["salles"].append(salle.__dict__)
            save_data("data.json", data)
            messagebox.showinfo("Succès", "Salle ajoutée avec succès.")
            popup.destroy()
        else:
            messagebox.showerror("Erreur", "Champs invalides")

    tk.Button(popup, text="Valider", command=valider).pack(pady=10)

# === Fenêtre pour ajouter un client ===
def ajouter_client_ui():
    window = tk.Toplevel()
    window.title("Ajouter un client")

    tk.Label(window, text="Nom :").pack()
    entry_nom = tk.Entry(window)
    entry_nom.pack()
    
    tk.Label(window, text="Prénom :").pack()
    entry_email = tk.Entry(window)
    entry_email.pack()

    tk.Label(window, text="Adresse email :").pack()
    entry_email = tk.Entry(window)
    entry_email.pack()

    def enregistrer():
        nom = entry_nom.get()
        email = entry_email.get()
        if nom and email:
            client = Client(nom, email)
            data = load_data("data.json")
            data["clients"].append(client.__dict__)
            save_data("data.json", data)
            messagebox.showinfo("Succès", "Client ajouté avec succès.")
            window.destroy()
        else:
            messagebox.showerror("Erreur", "Veuillez remplir tous les champs.")

    tk.Button(window, text="Enregistrer", command=enregistrer).pack(pady=10)

# === Fenêtre principale ===
def launch_app():
    root = tk.Tk()
    root.title("Gestion de réservation - MeetingPro")
    root.geometry("500x400")

    notebook = ttk.Notebook(root)
    notebook.pack(expand=True, fill='both')

    accueil_frame = ttk.Frame(notebook)
    ajouter_frame = ttk.Frame(notebook)
    reserver_frame = ttk.Frame(notebook)
    afficher_frame = ttk.Frame(notebook)

    notebook.add(accueil_frame, text="Accueil")
    notebook.add(ajouter_frame, text="Ajouter")
    notebook.add(reserver_frame, text="Réserver")
    notebook.add(afficher_frame, text="Afficher")

    # Accueil
    tk.Button(accueil_frame, text="Ajouter", width=30, height=2, command=lambda: notebook.select(1)).pack(pady=15)
    tk.Button(accueil_frame, text="Réserver", width=30, height=2, command=lambda: notebook.select(2)).pack(pady=15)
    tk.Button(accueil_frame, text="Afficher", width=30, height=2, command=lambda: notebook.select(3)).pack(pady=15)

    # Ajouter
    tk.Button(ajouter_frame, text="Ajouter nouveau client", width=30, height=2, bg="#125873", fg="white", command=ajouter_client_ui).pack(pady=25)
    tk.Button(ajouter_frame, text="Ajouter nouvelle salle", width=30, height=2, bg="#125873", fg="white", command=ajouter_salle_ui).pack(pady=10)

    root.mainloop()

# === Lancer le programme ===
if __name__ == "__main__":
    launch_app()
