# Demander à l'utilisateur de saisir des nombres séparés par des "@"
input_string = input("Entrez des nombres séparés par des '@' : ")

# Séparer la chaîne d'entrée en utilisant "@" comme séparateur
numbers_str_list = input_string.split("@")

# Convertir chaque élément de la liste de chaînes en entier
numbers_list = [int(num) for num in numbers_str_list]

# Classer les nombres par ordre décroissant
numbers_list.sort(reverse=True)

# Afficher la liste classée
print("Liste des nombres triés par ordre décroissant :", numbers_list)
