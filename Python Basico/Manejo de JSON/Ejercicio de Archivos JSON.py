import json


def read_file():
    try:
        with open("Pokemon List.json", 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("El archivo está corrupto. Se iniciará una lista nueva.")
        return []


def save_list(pokemons_list):
    with open("Pokemon List.json", 'w', encoding='utf-8') as file:
        json.dump(pokemons_list, file, ensure_ascii=False, indent=4)


def add_new_pokemon(path):
    pokemons = read_file()
    print("--- Agregar nuevo Pokémon ---")
    new_pokemon = {
        "name": input("Ingresa el nombre del Pokémon: ").strip(),
        "type": input("Ingresa el tipo de Pokémon: ").strip(),
        "level": int(input("Ingresa el nivel del Pokémon: ").strip()),
        "weight_kg": float(input("Ingresa el peso del Pokémon: ").strip()),
        "is_shiny": bool(input("¿Es shiny? (Yes/No): ").strip() == 'Yes'),
        "held_item": input("Ingresa el objeto que sostiene (o presiona Enter para omitir): ").strip() or None,
        "skills": [skill.strip() for skill in input("Ingresa las habilidades del Pokémon separadas por comas: ").split(',') if skill.strip()],
        "stats": {
            "hp": int(input("Ingresa los puntos de vida (HP): ").strip()),
            "attack": int(input("Ingresa el ataque: ").strip()),
            "defense": int(input("Ingresa la defensa: ").strip()),
            "sp_attack": int(input("Ingresa el ataque especial: ").strip()),
            "sp_defense": int(input("Ingresa la defensa especial: ").strip()),
            "speed": int(input("Ingresa la velocidad: ").strip())
        }
    }
    pokemons.append(new_pokemon)
    save_list(pokemons)
    print(f"¡El Pokémon '{new_pokemon['name']}' ha sido guardado exitosamente en {path}!")


if __name__ == "__main__":
    add_new_pokemon("Pokemon List.json")