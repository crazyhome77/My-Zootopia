import json


def load_data(file_path):
    """ Daten aus Json File laden """
    with open(file_path, "r") as handle:
        return json.load(handle)


def create_animals_string(animals_data):
    """ Erzeugt einen langen String mit allen Tier-Informationen """
    output = ''
    for animal in animals_data:
        # Extraktion der Felder (mit Sicherheitsprüfung via .get())
        name = animal.get('name')
        characteristics = animal.get('characteristics', {})
        diet = characteristics.get('diet')
        locations = animal.get('locations', [])
        animal_type = characteristics.get('type')

        # String mit Zeilenumbruch (\n)
        if name:
            output += f"Name: {name}\n"
        if diet:
            output += f"Diet: {diet}\n"
        if locations:
            output += f"Location: {locations[0]}\n"
        if animal_type:
            output += f"Type: {animal_type}\n"

        # Ein zusätzlicher Umbruch für den Abstand in der HTML-Ausgabe
        output += "\n"
    return output


def main():
    # 1. Daten laden
    animals_data = load_data('animals_data.json')

    # 2. Tier-String erstellen
    animals_info_string = create_animals_string(animals_data)

    # 3. Vorlage lesen
    with open("animals_template.html", "r") as f:
        template_content = f.read()

    # 4. Platzhalter ersetzen
    final_html = template_content.replace("__REPLACE_ANIMALS_INFO__", animals_info_string)

    # 5. Neue Datei schreiben
    with open("animals.html", "w") as f:
        f.write(final_html)

    print("Die Datei 'animals.html' wurde erfolgreich erstellt!")

if __name__ == "__main__":
    main()
