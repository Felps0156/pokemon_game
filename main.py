from api.pokeapi import get_random_pokemon
from models import Player


print("Qual será o nome do jogador?")
name_player = input("> ")

player = Player(
    name=name_player,
    pokecoin=0,
    pokemons=[]
)
while True:  
    print("[1] Sortear Pokemon ")
    choice = input("> ")
    
    if choice == "1":
        pokemon, rarity = get_random_pokemon()
        player.pokemons.append(pokemon.name)

        print(f"Você sorteou {pokemon.name}")
        print(f"Raridade: {rarity}")
        print(f"Vc possui: {player.pokemons}")