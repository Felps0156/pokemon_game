from api.pokeapi import get_pokemon
from pokemon import get_random_pokemon
from jogador import Jogador

print("Qual será o nome do jogador?")
Jogador.name = input("> ")

while True:
    print("Qual será o nome do jogador?")
    Jogador.name = input("> ")
    
    print("[1] Sortear Pokemon ")
    choice = input("> ")
    
    if choice == "1":
        rarity = get_random_pokemon()
        Jogador.pokemons = pokemon = get_random_pokemon()
        print(f"Você sorteou {pokemon}")
        print(f"Raridade: {rarity}")
        
        print(f"Voce tem {Jogador.pokemons}")