import turtle
import tkinter as tk
from tkinter import simpledialog, messagebox

def draw_letter(letter, color):
    """Dessine une lettre avec une couleur spécifiée."""
    turtle.color(color)
    turtle.write(letter, font=("Arial", 48, "normal"))
    turtle.forward(50)  # Espace entre les lettres

def draw_name(name, colors):
    """Dessine chaque lettre du nom avec une couleur différente."""
    for i, letter in enumerate(name):
        color = colors[i % len(colors)]  # Utiliser une couleur différente pour chaque lettre
        draw_letter(letter, color)

def get_name():
    """Demander à l'utilisateur d'entrer son nom."""
    nom = simpledialog.askstring("Entrer votre nom", "Quel est votre nom?")
    if not nom or not nom.isalpha():
        messagebox.showerror("Erreur", "Veuillez entrer uniquement des lettres.")
        return get_name()
    return nom

def change_name():
    """Fonction appelée lorsque l'utilisateur souhaite changer le nom."""
    global nom
    new_name = get_name()
    if new_name:
        nom = new_name
        turtle.clear()  # Effacer le dessin précédent
        draw_name(nom, colors)

def main():
    global nom, colors

    # Initialiser la fenêtre Tkinter
    root = tk.Tk()
    root.withdraw()  # Cacher la fenêtre principale

    # Demander à l'utilisateur d'entrer son nom via une boîte de dialogue
    nom = get_name()

    # Configuration initiale de la tortue
    turtle.speed(1)
    turtle.penup()
    turtle.goto(-200, 0)
    turtle.pendown()

    # Couleurs à utiliser pour dessiner le nom
    colors = ["blue", "green", "red", "orange", "purple"]  # Ajouter des couleurs si nécessaire
    
    # Écrire le nom avec des couleurs différentes pour chaque lettre
    draw_name(nom, colors)

    # Ajouter un bouton pour permettre à l'utilisateur de changer le nom
    change_button = tk.Button(root, text="Changer le nom", command=change_name)
    change_button.pack(pady=10)

    # Lancer la boucle principale de l'interface graphique
    root.mainloop()

if __name__ == "__main__":
    main()
