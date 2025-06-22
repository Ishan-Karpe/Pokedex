import json, os

class Pokémon:
    def __init__(self, name: str, id: int, types: list[str], evolution: str):
        self.name = name
        self.id = id
        self.types = types
        self.evolution = evolution