from api.pokeapi import get_pokemon
from api.pokeapi import get_random_pokemon
from models import Jogador, Pokemon

# print("Qual será o nome do jogador?")
# Jogador.name = input("> ")


while True:  
    print("[1] Sortear Pokemon ")
    choice = input("> ")
    
    if choice == "1":
        pokemon, rarity = get_random_pokemon()
        print(f"Você sorteou {pokemon}")
        print(f"Raridade: {rarity}")