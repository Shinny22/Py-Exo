import emoji # type: ignore

# Définir un dictionnaire contenant des célébrations
celebrations = {
    "Nouvel an": "1 Janvier",
    "Tabaski": "10 Juillet",
    "Pentecote": "5 Juin"
}

def normalize_date(day, month):
    """Normalise le format de la date pour comparaison."""
    normalized_month = month.lower().capitalize()
    return f"{day} {normalized_month}"

def main():
    print(emoji.emojize("🎉 Bienvenue dans le programme de vérification des célébrations 🎉\n"))

    # Demander à l'utilisateur de saisir le jour et le mois
    day = input("Veuillez entrer le jour (ex: 1): ").strip()
    month = input("Veuillez entrer le mois (ex: Janvier): ").strip()

    # Normaliser la date saisie
    date_saisie = normalize_date(day, month)

    # Vérifier si la date saisie correspond à une date de célébration
    found = False
    for celebration, date in celebrations.items():
        if date_saisie == date:
            print(emoji.emojize(f"🎊 Cette date correspond à la célébration : {celebration} 🎊"))
            found = True
            break

    if not found:
        print(emoji.emojize("❌ Cette date ne correspond à aucune célébration ❌"))

if __name__ == "__main__":
    main()
