import turtle

def draw_letter(letter, color):
    """Dessine une lettre avec une couleur spécifiée."""
    turtle.color(color)
    turtle.write(letter, font=("Arial", 48, "normal"))
    turtle.penup()
    turtle.forward(50)  # Espace entre les lettres
    turtle.pendown()

def draw_name(name, color):
    """Dessine chaque lettre du nom avec la couleur spécifiée."""
    for letter in name:
        draw_letter(letter, color)

def main():
    # Demander à l'utilisateur d'entrer son nom
    nom = input("Entrez votre nom: ")
    
    # Valider que l'entrée est une chaîne de caractères alphabetique
    while not nom.isalpha():
        print("Erreur : Veuillez entrer uniquement des lettres.")
        nom = input("Entrez votre nom: ")

    # Configuration initiale de la tortue
    turtle.speed(1)
    turtle.penup()
    turtle.goto(-200, 0)
    turtle.pendown()

    # Couleur à utiliser pour dessiner le nom
    couleur = "blue"
    
    # Écrire le nom
    draw_name(nom, couleur)

    # Fin du dessin
    turtle.hideturtle()
    turtle.done()

if __name__ == "__main__":
    main()
