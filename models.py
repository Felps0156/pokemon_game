class Jogador:
    def __init__(self, name, pokecoin, pokemons):
        self.name = name
        self.pokecoin = pokecoin
        self.pokemons = pokemons
        
class Pokemon:
    def __init__(self, name, types, stats, moves):
        self.name = name
        self.types = types
        self.stats = stats
        self.moves = moves