import requests
import random

from models import Pokemon, Player


rarities_pokemons = {
    "comum": [
        "rattata",
        "pidgey",
        "caterpie",
        "weedle",
        "zubat",
        "geodude",
        "magikarp"
    ],

    "incomum": [
        "pikachu",
        "growlithe",
        "machop",
        "gastly",
        "abra",
        "eevee"
    ],

    "raro": [
        "charizard",
        "lapras",
        "snorlax",
        "dragonair",
        "scyther",
        "gyarados"
    ],

    "epico": [
        "dragonite",
        "tyranitar",
        "metagross",
        "garchomp",
        "salamence"
    ],

    "lendario": [
        "mewtwo",
        "articuno",
        "zapdos",
        "moltres",
        "lugia",
        "rayquaza"
    ],

    "mitico": [
        "mew",
        "celebi",
        "jirachi",
        "deoxys"
    ]
}


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


def get_random_pokemon():
    rarities = [
        "comum",
        "incomum",
        "raro",
        "epico",
        "lendario",
        "mitico"
    ]

    rarity = random.choices(
        rarities,
        weights=[60, 20, 10, 7, 2.5, 0.5],
        k=1
    )[0]

    pokemon = random.choice(rarities_pokemons[rarity])
    
    pokemon_api = get_pokemon(name_pokemon=pokemon)
    return pokemon_api, rarity