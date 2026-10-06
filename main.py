from api.pokeapi import get_pokemon

pokemon = get_pokemon("charizard")
print(pokemon.stats)