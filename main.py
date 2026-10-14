import time

from api.pokeapi import get_random_pokemon
from screen import clean_screen, return_screen
from models import Player

# print("Qual será o nome do player?")
# name_player = input("> ")

player = Player(
    name="Felipe",
    pokecoin=1,
    pokemons=[]
)
while True: 
    clean_screen()
    
    print(f"Player: {player.name}")
    print(f"Pokecoin: {player.pokecoin}")
    print("-" * 15)
    
    print("[1] Sortear Pokemon ")
    print("[2] PC")
    
    choice = input("> ")
    
    if choice == "1":
        clean_screen()
        if player.pokecoin >= 1:
            player.pokecoin -= 1
            
            pokemon, rarity = get_random_pokemon()
            player.pokemons.append(pokemon.name)

            print(f"Você sorteou {pokemon.name}")
            print(f"Raridade: {rarity}")

            print(f"Quantidade de moedas: {player.pokecoin}")
            
            return_screen()
        else:
            print("Você não possui mais Moedas")
            return_screen()
        
    if choice == "2":
        clean_screen()
        
        print("-" * 15)
        print("  INVENTARIO")
        print("-" * 15)
        
        for pokemon in player.pokemons:
            print(pokemon)
            
        return_screen()