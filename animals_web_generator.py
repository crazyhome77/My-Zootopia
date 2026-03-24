import json


def load_data(file_path):
    """ Daten aus Json File laden """
    with open(file_path, "r") as handle:
        return json.load(handle)


def serialize_animal(animal_obj):
    """Serialisierung eines Tierobjekts in HTML """
    # Daten mit .get() extrahieren
    name = animal_obj.get('name')
    characteristics = animal_obj.get('characteristics', {})
    diet = characteristics.get('diet')
    locations = animal_obj.get('locations', [])
    animal_type = characteristics.get('type')

    # HTML-String für eine Karte
    output = '    <li class="cards__item">\n'

    # Titel der Karte
    if name:
        output += f'      <div class="card__title">{name}</div>\n'

    # Inhalt der Karte
    output += '      <p class="card__text">\n'

    if diet:
        output += f'          <strong>Diet:</strong> {diet}<br/>\n'
    if locations:
        output += f'          <strong>Location:</strong> {locations[0]}<br/>\n'
    if animal_type:
        output += f'          <strong>Type:</strong> {animal_type}<br/>\n'

    output += '      </p>\n'
    output += '    </li>\n'

    return output


def main():
    # 1. Daten laden
    animals_data = load_data('animals_data.json')

    # 2. HTML-String durch Iteration aufbauen
    output = ''
    for animal_obj in animals_data:
        output += serialize_animal(animal_obj)

    # 3. Vorlage lesen
    with open("animals_template.html", "r") as f:
        template_content = f.read()

    # 4. Platzhalter ersetzen
    final_html = template_content.replace("__REPLACE_ANIMALS_INFO__", output)

    # 5. Neue Datei schreiben
    with open("animals.html", "w") as f:
        f.write(final_html)

    print("Die Datei 'animals.html' wurde erfolgreich erstellt!")

if __name__ == "__main__":
    main()
