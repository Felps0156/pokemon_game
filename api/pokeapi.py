import requests
from pokemon import Pokemon

def get_pokemon(name_pokemon):
    url = f"https://pokeapi.co/api/v2/pokemon/{name_pokemon}/"
    
    response = requests.get(url)
    
    pokemon = response.json()
    
    types = []
    
    for type in pokemon["types"]:
        types.append(type["type"]["name"])
    
    
    stats = {}

    for stat in pokemon["stats"]:
        stats[stat["stat"]["name"]] = stat["base_stat"]
        

    moves = []

    for move in pokemon["moves"]:
        moves.append(move["move"]["name"])
        
        
    return Pokemon(
        name=pokemon["name"],
        types=types,
        stats=stats,
        moves=moves
    )
    