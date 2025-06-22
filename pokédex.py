import json, os

class Pokémon:
    def __init__(self, name: str, id: int, types: list[str], evolution: str):
        self.name = name
        self.id = id
        self.types = types
        self.evolution = evolution

    def to_dict(self):
        return {
            "name": self.name,
            "id": self.id,
            "types": self.types,
            "evolution": self.evolution
        }
    
pokédex = []

DATA_PATH = "pokemons.json" # constants for file paths

def load_pokédex():
    global pokédex
    if os.path.exists(DATA_PATH):
        with open(DATA_PATH, 'r') as file:
            try:
                data = json.load(file)
                pokédex = [Pokémon(**item) for item in data] # for each item in the JSON data, create a Pokémon object
            except json.JSONDecodeError:
                pokédex = []
    else:
        pokédex = []

def save_pokédex():
    with open(DATA_PATH, 'w') as file:
        json.dump([pokemon.to_dict() for pokemon in pokédex], file, indent=4)
        # Save the pokédex to a JSON file with indentation for readability

def add_pokemon():
    name = input("Enter Pokémon name: ")
    id = int(input("Enter Pokémon ID: "))
    if not id.isnumeric():
        print("ID must be a number.")
        return
    types = input("Enter Pokémon types (comma separated): ").split(',')
    evolution = input("Enter Pokémon evolution: ")
    
    new_pokemon = Pokémon(name.strip(), id, [t.strip() for t in types], evolution.strip())
    pokédex.append(new_pokemon)
    save_pokédex()
    print(f"{name} has been added to the Pokédex.")

def search_pokemon():
    name = input('Enter Pokémon name to search: ')
    for pokemon in pokédex:
        if pokemon.name.lower() == name.lower():
            print(f"Found Pokémon: {pokemon.name}, ID: {pokemon.id}, Types: {', '.join(pokemon.types)}, Evolution: {pokemon.evolution}")
            return
    print("Pokémon not found.")

def view_all():
    if not pokédex:
        print("Pokédex is empty.")
        return
    else:
        for pokemon in pokédex:
            print(f"Name: {pokemon.name}, ID: {pokemon.id}, Types: {', '.join(pokemon.types)}, Evolution: {pokemon.evolution}")

def main():
    load_pokédex()
    while True:
        print("\n Pokédex Menu:")
        print("1. Add Pokémon")
        print("2. Search Pokémon")
        print("3. View All Pokémon")
        print("4. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            add_pokemon()
        elif choice == 2:
            search_pokemon()
        elif choice == 3:
            view_all()
        elif choice == 4:
            print("Exiting Pokédex.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()