# Liste de coordonnées de points x, y
coordinates = [(4,5), (9,3), (12,8), (13,7), (18,6), (20,9)]

# Remplissage de la liste d'ordonnées avec compréhension de liste
ordinates = [7 if y > 7 else y for x, y in coordinates]

# Affichage de la liste d'ordonnées
print("Liste des ordonnées:", ordinates)

# Création d'un dictionnaire à partir de la liste de coordonnées
dict_coordinates = dict(coordinates)

# Mise à jour des ordonnées dans le dictionnaire avec compréhension de dictionnaire
dict_coordinates = {key: 7 if value > 7 else value for key, value in dict_coordinates.items()}

# Affichage des coordonnées mises à jour
print("Coordonnées mises à jour:", list(dict_coordinates.items()))


