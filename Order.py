try:
    # Demander à l'utilisateur de saisir des nombres séparés par des '@'
    input_string = input("Entrez des nombres séparés par des '@' : ")

    # Vérifier si la chaîne est vide
    if not input_string:
        raise ValueError("La chaîne d'entrée est vide.")

    # Séparer la chaîne d'entrée en utilisant "@" comme séparateur
    numbers_str_list = input_string.split("@")

    # Convertir chaque élément de la liste de chaînes en entier
    numbers_list = []
    for num_str in numbers_str_list:
        try:
            num = int(num_str)
            numbers_list.append(num)
        except ValueError:
            print(f"Attention : '{num_str}' n'est pas un nombre entier et sera ignoré.")

    # Classer les nombres par ordre décroissant
    numbers_list.sort(reverse=True)

    # Afficher la liste classée
    if numbers_list:
        print("Liste des nombres triés par ordre décroissant :", numbers_list)
    else:
        print("Aucun nombre valide n'a été saisi.")
except Exception as e:
    print("Erreur :", e)
