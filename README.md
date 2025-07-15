# Pokédex

## Features:
1. ✅ Add new Pokémon with validation
2. 🔍 Search Pokémon by name or ID
3. 🗑️ Remove Pokémon with confirmation
4. 📋 View all Pokémon
5. 💾 Persistent storage using JSON
6. 🛡️ Input validation and error handling

### Setup:
- I have created a pypi package: https://pypi.org/project/pokedex-python/0.0.1/

install it and follow this:

```
from pokedex_python import pokédex

pokédex.main()
``` 
### Structure:
Pokedex/
├── pokédex.py          # Main application file
├── pokemons.json       # Data storage (created automatically)
├── README.md           # This file
└── requirements.txt    # Dependencies

### Sample Usage:
Enter Pokémon name: Pikachu
Enter Pokémon ID: 25
Enter Pokémon types (comma separated): electric
Enter Pokémon evolution: Raichu

A Pikachu has been added to the Pokédex.


