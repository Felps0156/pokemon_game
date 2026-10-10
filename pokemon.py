import random

class Pokemon:
    def __init__(self, name, types, stats, moves):
        self.name = name
        self.types = types
        self.stats = stats
        self.moves = moves

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
        weights=[60, 20, 10, 7, 1, 0.5],
        k=1
    )[0]

    pokemon = random.choice(rarities_pokemons[rarity])

    return pokemon, rarity

