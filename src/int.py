import tkinter as tk
from tkinter import ttk, messagebox
from models import Client, Salle
from database import load_data, save_data
from datetime import datetime


# === Fenêtre pour ajouter un client ===
def ajouter_client_ui():
    window = tk.Toplevel()
    window.title("Ajouter un client")

    tk.Label(window, text="Nom :").pack()
    entry_nom = tk.Entry(window)
    entry_nom.pack()
    
    tk.Label(window, text="Prénom :").pack()
    entry_prenom = tk.Entry(window)
    entry_prenom.pack()

    tk.Label(window, text="Adresse email :").pack()
    entry_email = tk.Entry(window)
    entry_email.pack()

    def valider():
        nom = entry_nom.get().strip()
        prenom = entry_prenom.get().strip()
        email = entry_email.get().strip()

        if not nom or not prenom or not email:
            messagebox.showerror("Erreur", "Tous les champs sont obligatoires.")
            return

        if "@" not in email or "." not in email:
            messagebox.showerror("Erreur", "Adresse email invalide.")
            return

        client = Client(nom + " " + prenom, email)
        data = load_data("data.json")
        data["clients"].append(client.__dict__)
        save_data("data.json", data)
        messagebox.showinfo("Succès", "Client ajouté avec succès.")
        window.destroy()

    def annuler():
        window.destroy()

    bouton_frame = tk.Frame(window)
    bouton_frame.pack(pady=10)

    tk.Button(bouton_frame, text="Valider", width=12, bg="#28a745", fg="white", command=valider).pack(side=tk.LEFT, padx=5)
    tk.Button(bouton_frame, text="Annuler", width=12, bg="#dc3545", fg="white", command=annuler).pack(side=tk.LEFT, padx=5)


# === Fenêtre pour ajouter une salle ===
def ajouter_salle_ui():
    window = tk.Toplevel()
    window.title("Ajouter une salle")

    tk.Label(window, text="Identifiant de la salle :").pack(pady=(10,0))
    entry_id = tk.Entry(window)
    entry_id.pack()

    tk.Label(window, text="Type de salle :").pack(pady=(10,0))
    types = ["Standard", "Conférence", "Informatique"]
    combo_type = ttk.Combobox(window, values=types, state="readonly")
    combo_type.current(0)  # valeur par défaut
    combo_type.pack()

    tk.Label(window, text="Capacité :").pack(pady=(10,0))
    entry_capacite = tk.Entry(window)
    entry_capacite.pack()

    def valider():
        id_salle = entry_id.get().strip()
        type_salle = combo_type.get()
        capacite = entry_capacite.get().strip()

        if not id_salle:
            messagebox.showerror("Erreur", "L'identifiant est obligatoire.")
            return
        if not capacite.isdigit() or int(capacite) <= 0:
            messagebox.showerror("Erreur", "La capacité doit être un nombre entier positif.")
            return

        data = load_data("data.json")

        # Vérifier unicité identifiant
        ids_existants = [s["identifiant"] for s in data["salles"]]
        if id_salle in ids_existants:
            messagebox.showerror("Erreur", f"L'identifiant '{id_salle}' existe déjà. Veuillez en choisir un autre.")
            return

        # Ajouter la salle
        salle = Salle(id_salle, type_salle, int(capacite))
        data["salles"].append(salle.__dict__)
        save_data("data.json", data)
        messagebox.showinfo("Succès", "Salle ajoutée avec succès.")
        window.destroy()

        # Retour à l'onglet Accueil (index 0)
        notebook.select(0)

    def annuler():
        window.destroy()

    bouton_frame = tk.Frame(window)
    bouton_frame.pack(pady=15)
    tk.Button(bouton_frame, text="Valider", width=12, bg="#28a745", fg="white", command=valider).pack(side=tk.LEFT, padx=5)
    tk.Button(bouton_frame, text="Annuler", width=12, bg="#dc3545", fg="white", command=annuler).pack(side=tk.LEFT, padx=5)

#FENETRE POUR RESRVER SALLE 
def reserver_salle_ui(parent):
    from datetime import datetime

    tk.Label(parent, text="Date de début (jj/mm/aaaa hh:mm)").pack(pady=5)
    entry_debut = tk.Entry(parent, width=30)
    entry_debut.pack()

    tk.Label(parent, text="Date de fin (jj/mm/aaaa hh:mm)").pack(pady=5)
    entry_fin = tk.Entry(parent, width=30)
    entry_fin.pack()

    tk.Label(parent, text="Client :").pack(pady=5)
    search_var = tk.StringVar()
    entry_search = tk.Entry(parent, textvariable=search_var, width=30)
    entry_search.pack()

    combo_client = ttk.Combobox(parent, width=30)
    combo_client.pack()

    data = load_data("data.json")
    clients = [client["nom"] for client in data.get("clients", [])]
    combo_client["values"] = clients

    def filtrer_clients(*args):
        recherche = search_var.get().lower()
        resultat = [c for c in clients if recherche in c.lower()]
        combo_client["values"] = resultat

    search_var.trace_add("write", filtrer_clients)

    tk.Label(parent, text="Type de salle :").pack(pady=5)
    type_var = tk.StringVar(value="Standard")
    for t in ["Standard", "Conférence", "Informatique"]:
        tk.Radiobutton(parent, text=t, variable=type_var, value=t).pack(anchor="w", padx=20)

    tk.Label(parent, text="Salle disponible :").pack(pady=5)
    combo_salle = ttk.Combobox(parent, width=30, state="readonly")
    combo_salle.pack()

    etat = {"salles_chargees": False}

    def valider():
        debut = entry_debut.get().strip()
        fin = entry_fin.get().strip()
        client_nom = combo_client.get().strip()

        if not etat["salles_chargees"]:
            # === Étape 1 : vérifier et charger les salles ===
            if not debut or not fin or not client_nom:
                messagebox.showerror("Erreur", "Tous les champs doivent être remplis.")
                return

            try:
                date_debut = datetime.strptime(debut, "%d/%m/%Y %H:%M")
                date_fin = datetime.strptime(fin, "%d/%m/%Y %H:%M")
            except:
                messagebox.showerror("Erreur", "Format de date invalide.")
                return

            if date_fin <= date_debut:
                messagebox.showerror("Erreur", "La date de fin doit être après la date de début.")
                return

            data = load_data("data.json")
            type_salle = type_var.get()
            salles_dispo = []

            for salle in data["salles"]:
                if salle["type_salle"] != type_salle:
                    continue

                conflits = False
                for res in data["reservations"]:
                    if res["id_salle"] == salle["identifiant"]:
                        res_debut = datetime.strptime(res["debut"], "%d/%m/%Y %H:%M")
                        res_fin = datetime.strptime(res["fin"], "%d/%m/%Y %H:%M")
                        if not (date_fin <= res_debut or date_debut >= res_fin):
                            conflits = True
                            break

                if not conflits:
                    salles_dispo.append(salle["identifiant"])

            combo_salle["values"] = salles_dispo
            etat["salles_chargees"] = True

            if not salles_dispo:
                messagebox.showwarning("Aucune salle", "Aucune salle disponible pour ce créneau.")
            else:
                messagebox.showinfo("Salles disponibles", "Veuillez sélectionner une salle et cliquer à nouveau sur Valider.")
        else:
            # === Étape 2 : Enregistrement + résumé ===
            salle_choisie = combo_salle.get().strip()
            if not salle_choisie:
                messagebox.showerror("Erreur", "Veuillez sélectionner une salle.")
                return

            reservation = {
                "client": client_nom,
                "id_salle": salle_choisie,
                "debut": debut,
                "fin": fin
            }
            data["reservations"].append(reservation)
            save_data("data.json", data)

            # === Résumé ===
            for salle in data["salles"]:
                if salle["identifiant"] == salle_choisie:
                    capacite = salle["capacite"]
                    type_salle = salle["type_salle"]
                    break

            delta = datetime.strptime(fin, "%d/%m/%Y %H:%M") - datetime.strptime(debut, "%d/%m/%Y %H:%M")
            duree = int(delta.total_seconds() // 3600)

            resume = tk.Toplevel()
            resume.title("Réservation Validée!")

            tk.Label(resume, text="✅ Réservation confirmée !", font=("Arial", 14, "bold"), fg="#28a745").pack(pady=10)
            infos = f"""\
Client : {client_nom}
Début : {debut}
Fin : {fin}
Salle : {salle_choisie}
Durée : {duree}h
Type : {type_salle}
Capacité : {capacite}"""
            tk.Label(resume, text=infos, justify="left", font=("Arial", 11)).pack(padx=20, pady=10)
            tk.Button(resume, text="Menu principal", bg="#007bff", fg="white", width=20, command=resume.destroy).pack(pady=10)

            # Nettoyage
            entry_debut.delete(0, tk.END)
            entry_fin.delete(0, tk.END)
            entry_search.delete(0, tk.END)
            combo_client.set("")
            combo_salle.set("")
            etat["salles_chargees"] = False

    def annuler():
        entry_debut.delete(0, tk.END)
        entry_fin.delete(0, tk.END)
        entry_search.delete(0, tk.END)
        combo_client.set("")
        combo_salle.set("")
        etat["salles_chargees"] = False

    bouton_frame = tk.Frame(parent)
    bouton_frame.pack(pady=10)
    tk.Button(bouton_frame, text="Valider", width=15, bg="#28a745", fg="white", command=valider).pack(side=tk.LEFT, padx=5)
    tk.Button(bouton_frame, text="Annuler", width=15, bg="#dc3545", fg="white", command=annuler).pack(side=tk.LEFT, padx=5)

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
    
    reserver_salle_ui(reserver_frame)
    root.mainloop()

# === Lancer le programme ===
if __name__ == "__main__":
    launch_app()