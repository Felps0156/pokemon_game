from api.pokeapi import get_random_pokemon
from game.pc import open_pc
from game.menu import open_menu

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
        open_menu(player)
        
    if choice == "2":
        open_pc(player)