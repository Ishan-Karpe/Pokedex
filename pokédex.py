import json, os

class Pokémon:
    def __init__(self, name: str, id: int, types: list[str], evolution: str):
        self.name = name
        self.id = id
        self.types = types
        self.evolution = evolution

    def to_dict(self): # Convert the Pokémon object to a dictionary for easy JSON reading/writing
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
    with open(DATA_PATH, 'w') as file: # dump() is used to write the pokédex data to a JSON file
        json.dump([pokemon.to_dict() for pokemon in pokédex], file, indent=4) # Save the pokédex to a JSON file with indentation for readability

def add_pokemon():
    name = input("Enter Pokémon name: ")
    if name == '':
        print('Please give your Pokémon a name.')
        return 
    id = int(input("Enter Pokémon ID: "))
    if not id.isdigit() or id <= 0:
        print('Please provide an ID for your Pokémon.')
        return
    types = input("Enter Pokémon types (comma separated): ").split(',')
    if types == ['']:
        print('Please provide at least one type for your Pokémon.')
        return
    evolution = input("Enter Pokémon evolution: ")
    if evolution == '':
        print('Please provide an evolution for your Pokémon.')
        return


    for pokemon in pokédex:
        if pokemon.name.lower() == name.lower() or pokemon.id == id:
            print(f"A Pokémon with that name or ID already exists in your Pokédex!")
            return  # Exit the function to prevent adding a duplicate
    new_pokemon = Pokémon(name.strip(), int(id), [t.strip() for t in types], evolution.strip()) # Create a new Pokémon object with the provided details and append it to the pokédex
    pokédex.append(new_pokemon)
    save_pokédex()
    print(f"{name} has been added to the Pokédex.")

def search_pokemon():
    try:
        choice1 = int(input('Would you like to search by name (1) or id (2)? Enter 1 or 2 for your choice: '))
    except ValueError:
        print("Invalid choice. Please enter a number.")
        return

    if choice1 == 1:
        name = input('Enter Pokémon name to search: ')
        print(f'Searching for {name} in the Pokédex...')
        for pokemon in pokédex:
            if pokemon.name.lower() == name.lower():
                print(f"Found Pokémon: {pokemon.name}, ID: {pokemon.id}, Types: {', '.join(pokemon.types)}, Evolution: {pokemon.evolution}")
                return    #since it terminates no else is needed as if it fails it wont enter the loop
        print(f"Pokémon with name: {name} not found.")
    elif choice1 == 2:
        try:
            id_search = int(input('Enter Pokémon ID to search: '))
        except ValueError:
            print("Invalid ID. Please enter a number.")
            return
        print(f'Searching for {id_search} in the Pokédex...')
        for pokemon in pokédex:
            if pokemon.id == id_search:
                print(f"Found Pokémon: {pokemon.id}, Name: {pokemon.name}, Types: {', '.join(pokemon.types)}, Evolution: {pokemon.evolution}")
                return
        print(f"Pokémon with id: {id_search} not found.")
    else:
        print('Invalid choice, please try again.')


def remove_pokemon():
    pass


def main():
    load_pokédex()
    while True:
        print("\n Pokédex Menu:")
        print("1. Add Pokémon")
        print("2. Search Pokémon")
        print("3. Remove Pokémon")
        print("4. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            add_pokemon()
        elif choice == 2:
            search_pokemon()
        elif choice == 3:
            remove_pokemon()
        elif choice == 4:
            save_pokédex()
            print("Exiting Pokédex.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()


"""Now, Some lines may look confusing to new people so let me explain them, eli15:

Line 28: `pokédex = [Pokémon(**item) for item in data]` 
- This line takes each item in the list called 'data' (which is loaded from the JSON file) and turns it into a Pokémon object. It uses each key-value pair in the dictionary as arguments for the Pokémon class.

Line 36: `json.dump([pokemon.to_dict() for pokemon in pokédex], file, indent=4)` 
- This line converts each Pokémon object back into a dictionary using the `to_dict` method and writes it to the JSON file.

Line 47: `new_pokemon = Pokémon(name.strip(), int(id), [t.strip() for t in types], evolution.strip())`
- This line creates a new Pokémon object with the provided details and appends it to the pokédex. Strips whitespaces from the input.
"""