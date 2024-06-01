import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# Définir un dictionnaire contenant des célébrations
celebrations = {
    "Nouvel an": "1 Janvier",
    "Tabaski": "10 Juillet",
    "Pentecote": "5 Juin"
}

def normalize_date(day, month):
    """
    Normalise le format de la date pour comparaison.
    La fonction convertit le mois en minuscule et 
    capitalise la première lettre pour uniformité.
    """
    normalized_month = month.lower().capitalize()
    return f"{day} {normalized_month}"

def check_celebration():
    """
    Vérifie si la date saisie correspond à une célébration.
    Affiche une boîte de message en fonction du résultat.
    """
    day = entry_day.get().strip()  # Récupère et nettoie l'entrée du jour
    month = entry_month.get().strip()  # Récupère et nettoie l'entrée du mois
    
    # Vérifier que les champs ne sont pas vides
    if not day or not month:
        messagebox.showerror("Erreur de saisie", "Veuillez remplir tous les champs.")
        return

    # Vérifier que le jour est un nombre entier
    if not day.isdigit():
        messagebox.showerror("Erreur de saisie", "Le jour doit être un nombre entier.")
        return
    
    # Normaliser la date saisie
    date_saisie = normalize_date(day, month)
    
    # Rechercher la date dans le dictionnaire des célébrations
    found = False
    for celebration, date in celebrations.items():
        if date_saisie == date:
            result_text.config(state=tk.NORMAL)
            result_text.delete("1.0", tk.END)
            result_text.insert(tk.END, f"🎊 Cette date correspond à la célébration : {celebration} 🎊\n")
            result_text.config(state=tk.DISABLED)
            found = True
            break

    # Si la date n'est pas trouvée, afficher un message d'erreur
    if not found:
        result_text.config(state=tk.NORMAL)
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, "❌ Cette date ne correspond à aucune célébration ❌\n")
        result_text.config(state=tk.DISABLED)

# Configuration de l'interface graphique
root = tk.Tk()
root.title("Vérification des célébrations")
root.geometry("500x400")
root.config(bg="#f0f0f0")

# Style pour les widgets
style = ttk.Style()
style.configure("TEntry", padding=5, relief="flat", borderwidth=2)
style.configure("TButton", padding=5, relief="flat", borderwidth=2)
style.configure("TLabel", background="#f0f0f0")

# Créer les widgets
label_intro = tk.Label(root, text="🎉 Bienvenue dans le programme de vérification des célébrations 🎉", font=("Arial", 14, "bold"), bg="#f0f0f0", anchor="center")
label_day = tk.Label(root, text="Entrez le jour (ex: 1):", font=("Arial", 12, "bold"), bg="#f0f0f0")
entry_day = ttk.Entry(root, font=("Arial", 12), width=10)
label_month = tk.Label(root, text="Entrez le mois (ex: Janvier):", font=("Arial", 12, "bold"), bg="#f0f0f0")
entry_month = ttk.Entry(root, font=("Arial", 12), width=20)
check_button = ttk.Button(root, text="Vérifier la célébration", command=check_celebration, style="TButton")

# Zone de texte pour afficher les résultats
result_text = tk.Text(root, height=5, font=("Arial", 12), bg="#e0e0e0", state=tk.DISABLED)

# Disposer les widgets dans la fenêtre
label_intro.pack(pady=20, fill='x')
label_day.pack(pady=10)
entry_day.pack(pady=5)
label_month.pack(pady=10)
entry_month.pack(pady=5)
check_button.pack(pady=20)
result_text.pack(pady=20, fill='both', padx=10)

# Lancer la boucle principale de l'interface graphique
root.mainloop()
