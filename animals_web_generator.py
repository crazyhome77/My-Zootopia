import json


def load_data(file_path):
    """ Daten aus Json File laden """
    with open(file_path, "r") as handle:
        return json.load(handle)


def create_animals_html_string(animals_data):
    """Tier Infomrationen in HTML-Listen-Elemente wandeln (Serialisierung) """
    output = ''
    for animal in animals_data:
        # Daten extrahieren
        name = animal.get('name')
        characteristics = animal.get('characteristics', {})
        diet = characteristics.get('diet')
        locations = animal.get('locations', [])
        animal_type = characteristics.get('type')

        # Start des Listenelements (entspricht der CSS-Klasse in der Vorlage)
        output += '    <li class="cards__item">\n'

        # Felder einzeln hinzufügen, danach HTML-Zeilenumbruch <br/>
        if name:
            output += f"        Name: {name}<br/>\n"
        if diet:
            output += f"        Diet: {diet}<br/>\n"
        if locations:
            output += f"        Location: {locations[0]}<br/>\n"
        if animal_type:
            output += f"        Type: {animal_type}<br/>\n"

        # Ende des Listenelements
        output += '    </li>\n'

    return output


def main():
    # 1. Daten laden
    animals_data = load_data('animals_data.json')

    # 2. Tier-String erstellen
    animals_html_content = create_animals_html_string(animals_data)

    # 3. Vorlage lesen
    with open("animals_template.html", "r") as f:
        template_content = f.read()

    # 4. Platzhalter ersetzen
    final_html = template_content.replace("__REPLACE_ANIMALS_INFO__", animals_html_content)

    # 5. Neue Datei schreiben
    with open("animals.html", "w") as f:
        f.write(final_html)

    print("Die Datei 'animals.html' wurde erfolgreich erstellt!")

if __name__ == "__main__":
    main()
