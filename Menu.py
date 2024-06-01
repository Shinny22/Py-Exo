print("\033[1;35m")

print('  --------------------------------------------------------------------|  \n')
print('  |      BIENVENU Mr IBARA DANS LE PROGRAMME D\'IMMERSION A PYTHON    |  \n')
print('  |-------------------------------------------------------------------|  \n')

print('  |       1-  Ecrire son nom sur une interface graphique              |  \n')
print('  |       2-  Vérifier les dates de célébration                       |  \n')
print('  |       3-  Afficher on ordre les entiers entrés                    |  \n')
print('  |       4-  Travailler avec les coordonnées                         |  \n')
print('  |       5-  Travaillons les ensembles                               |  \n')
print('  |       0-  Quitter le programme                                    |  \n')
print('  --------------------------------------------------------------------\n\033[0m')

choice = int(input(' Faites vos choix :'))

while choice != 0:
    if choice == 1:
        try:
            exec(open('Name.py').read())
        except FileNotFoundError:
            print("Fichier 'Name.py' non trouvé.")
    elif choice == 2:
        try:
            exec(open('Celebration.py').read())
        except FileNotFoundError:
            print("Fichier 'Celebration.py' non trouvé.")
    elif choice == 3:
        try:
            exec(open('Order.py').read())
        except FileNotFoundError:
            print("Fichier 'Order.py' non trouvé.")
    elif choice == 4:
        try:
            exec(open('Coordo.py').read())
        except FileNotFoundError:
            print("Fichier 'Coordo.py' non trouvé.")
    elif choice == 5:
        try:
            exec(open('Ensemble.py').read())
        except FileNotFoundError:
            print("Fichier 'Ensemble.py' non trouvé.")
    else:
        print("Choix invalide, veuillez réessayer.")
    
    print("\033[1;35m")
    print('  --------------------------------------------------------------------|  \n')
    print('  |      BIENVENU Mr IBARA DANS LE PROGRAMME D\'IMMERSION A PYTHON    |  \n')
    print('  |-------------------------------------------------------------------|  \n')
    print('  |       1-  Ecrire son nom sur une interface graphique              |  \n')
    print('  |       2-  Vérifier les dates de célébration                       |  \n')
    print('  |       3-  Afficher on ordre les entiers entrés                    |  \n')
    print('  |       4-  Travailler avec les coordonnées                         |  \n')
    print('  |       5-  Travaillons les ensembles                               |  \n')
    print('  |       0-  Quitter le programme                                    |  \n')
    print('  --------------------------------------------------------------------\n\033[0m')

    choice = int(input(' Faites vos choix :'))

print("Programme terminé.")
