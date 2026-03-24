import json


def load_data(file_path):
    """ Daten aus Json File laden """
    with open(file_path, "r") as handle:
        return json.load(handle)


def display_animals(animals_data):
    """ Geht der Reihe nach alle Tiere durch und zeigt zu jedem bestimmte Informationen an """
    for animal in animals_data:
        # Extraktion der gewünschten Felder
        name = animal.get('name')
        characteristics = animal.get('characteristics', {})
        diet = characteristics.get('diet')
        locations = animal.get('locations', [])
        animal_type = characteristics.get('type')

        # Ausgabe, sofern das Feld existiert
        if name:
            print(f"Name: {name}")
        if diet:
            print(f"Diet: {diet}")
        if locations:
            # Nur den ersten Ort aus der Liste ausgeben
            print(f"Location: {locations[0]}")
        if animal_type:
            print(f"Type: {animal_type}")

        # Leerzeile zwischen den Tieren
        print("-" * 20)


def main():
    # Daten laden
    animals_data = load_data('animals_data.json')
    # Daten ausgeben
    display_animals(animals_data)


if __name__ == "__main__":
    main()
